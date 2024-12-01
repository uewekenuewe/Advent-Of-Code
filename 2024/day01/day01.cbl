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
       01  input-record-day01 redefines input-record.
           05 number1  pic 9(05).
           05 filler pic x(03).
           05 number2 pic 9(05).
       WORKING-STORAGE SECTION. 
       01  puzzle-input-name pic x(64) value './01'.
       01  puzzle-input-status pic x(2) value '00'.
       01  temp-rec pic x(80) value space.
       01  temp-rec-tab occurs 80 times pic x(01).
       01  result-tmp pic 9(10).
       01  result-temp pic x(80).
       01  resultA pic 9(10) value 0.
       01  resultB pic 9(10) value 0.
       01 list-number1.
           05 l-tab1 occurs 1000 times.
               10 l-num1 pic 9(05).
       01 list-number2.
           05 l-tab2 occurs 1000 times.
               10 l-num2 pic 9(05).
       01 list-number3.
           05 l-tab3 occurs 1000 times.
               10 l-num3 pic 9(05) value 0.
               10 l-num3-count pic 9(05) value 0.
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
               move number1 to l-num1(i)
               move number2 to l-num2(i)
           end-if
           end-perform

           sort l-tab1 descending l-num1
           sort l-tab2 descending l-num2

           perform varying j from 1 by 1 until j > 1000
               compute result-tmp = l-num1(j) - l-num2(j)
               if result-tmp < 0
                   compute resultA = resultA + (-1) * result-tmp
                else
                    compute resultA = resultA + result-tmp
                end-if
            end-perform

            perform varying i from 1 by 1 until i > 1000
                perform varying k from 1 by 1 until k > 1000
                    if l-num2(i) equal l-num3(k)
                        add 1 to l-num3-count(k)
                        move 1001 to k
                    else
                        if l-num3(k) equal 0
                            move l-num2(i) to l-num3(k)
                            add 1 to l-num3-count(k)
                            move 1001 to k
                        end-if
                    end-if
                end-perform
            end-perform


            perform varying i from 1 by 1 until i > 1000
                if l-num3(i) equal 0
                    exit perform
                end-if
            end-perform
            perform varying i from 1 by 1 until i > 1000
                perform varying k from 1 by 1  until k > 1000
                    if l-num1(i) equal l-num3(k)
                        compute resultB = resultB + (l-num3-count(k) *
                        l-num3(k))
                        end-compute
                        exit perform
                    end-if
                end-perform
            end-perform

           display "file count: " i
           close puzzle-input
           display "Day1 Part A: " resultA
           display "Day1 Part B: " resultB

           STOP RUN.
