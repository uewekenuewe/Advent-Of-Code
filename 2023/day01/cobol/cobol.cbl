       IDENTIFICATION DIVISION.
       PROGRAM-ID. AOC-Template.
       AUTHOR. Uwe Schmidt.
       environment division.
       input-output section.
       file-control.
           select puzzle-input
               assign to puzzle-input-name
               file status is puzzle-input-status
               organization is line sequential.

       data division.
       file section.
       fd  puzzle-input.
       01  input-record pic x(80).
       WORKING-STORAGE SECTION. 
       01  puzzle-input-name pic x(64) value './day1'.
       01  puzzle-input-status pic x(2) value '00'.
       01  temp-rec pic x(80) value space.
       01  temp-rec-tab occurs 80 times pic x(01).
       01  result-tmp pic 9(10).
       01  result-temp pic x(80).
       01  resultA pic 9(10) value 0.
       01 input-table.
           05 tab-rec occurs 1000 times pic x(80).
       01 result-table.
           05 result-rec occurs 1000 times pic 9(5).
       01 loop-vars.
           05 i pic 9(10) value 0.
           05 k pic 9(10)  value 0.
           05 j pic 9(10) comp-5 value 0.
           05 x pic 9(10) comp-5 value 0.
           05 y pic 9(10) comp-5 value 0.
       PROCEDURE DIVISION.
           open input puzzle-input
           perform with test after 
               until puzzle-input-status not equal '00'
               read puzzle-input
               if puzzle-input-status equal '00'
                   add 1 to i
               move input-record to tab-rec(i)
           end-if
           end-perform
           display "file count: " i
           close puzzle-input


           display "---"
           move 1 to k 
           move space to result-temp
           perform varying y from 1 by 1 until y > i
               display tab-rec(y)
               move space to result-temp
               move 1 to k
           perform varying x from 1 by 1 until x > 80
               if tab-rec(y)(x:1) not equal space
                   and tab-rec(y)(x:1) is numeric
                   move tab-rec(y)(x:1) to result-temp(k:1)
                   compute k = k + 1
                   exit perform
               end-if
           end-perform
           perform varying x from 80 by -1 until x equal 0
               if tab-rec(y)(x:1) not equal space
                   and tab-rec(y)(x:1) is numeric
               move tab-rec(y)(x:1) to result-temp(k:1)
               exit perform
           end-if
           end-perform
           add function numval( result-temp) to resultA
           end-perform

           display "---"

           display resultA

           STOP RUN.
       init section.
           initialize loop-vars
                    temp-rec
           exit.
