# -*- coding: UTF-8 -*-
import RSlib
import tkinter as tk
import shutil
from random import randint
from  tkinter import messagebox
from  tkinter import filedialog
import os
import pathlib
icon = "iVBORw0KGgoAAAANSUhEUgAAAQAAAADYCAYAAAAEaD2QAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAA4mUlEQVR42u29eXwc13Xn+z23qnrFvnEnRXHRSlKWZa2WbFkmZcmynZnYHmfsODMviy3bWV7ykjeZmTiZT5LP5DMvy4szHnkmmSSezHMS2/ISW3tkSV60LyRIiRQpLuICEsTeAHqtuuf9Ud1AAyQlLgABkPfLjwigUdVV1eL53XPOPfdcwXHB0LbtronvQ6kAAggGQyBJBIiICG0ZgMCk8MWnFBWICBEBRREEXwMUZXDTQ3P9WI5ZROb6BhxvT0P37Rj18EwCUSHSCgoEkiDUCopixKCqKBaLxVifxKJxygNZ46tvUl7WoGpCKqYcFURRUl6DTZqUzYejWrKFyE94tnXtUe17bRFS/ZchGAAUixGDJwGhLSHi4YlPRYsoFhBGNz4+1x+V4wxxAjDPaO6+E4DAJKlEJUAx4hFpxFihj67GtV4hHPEVmgMJWkOtNCIs8fCXW2yj1cgHEkAaSAEZkLQR0yBIRtGkVZuovm9JkHGrUVHRMWAcqFS/jgNqxKsAx61Gh42YAQ9/JNTykCfBeGtycdRXOGxFwIgh0gjfJFC1lBjDI+FEYZ7jBGCOaOreXHXQfVQtRjysRkRaJuFljBGvtRKVOkCXeeIviTTsQFgKcomqbQM6BOlSNAskQVKgs3W7EVACKQsMKnpckGER02s12i9IrxG/P9LKId8kjqnawaGND402bL2DwCSxRJiqJzEU7aPZW8nIxsfm+n+BAycA54XG7jtQtQSSwmoEgNUIq0rCS2WsRs3GeJdYG14CXA5cBrJG0eWgtZHbvP2VtO7vqa+hJ/8tSPyPYPIvpn534k8nRyqg44IZVvSAiOxDdYcR/w1LdMBgjopIrhwVy6YaPiiKLwH9hZdoTl3lRGEOcAIwC7R0b6nGzoIgWCyqFl+CRKiVxcB6EXOlqr1cYQ2wGugAbQZOaeiKxn9r/FMNT3w8E2DwEBEEgyc+viTwTYARv/pzgCc+RnwAIq0QaplIQyIbEmkl/l5DQq1Ur2UnXquJV4xU8wRSk5CTIkhF0UFBehXdY8Tfqxq9ZsTbA+xp9FsHR8KBSNVOnDM6Ck1NOEE4DzgBmAGau++kQgFRg08CRFBVMl7WK9tSp8Wut2pvFrhB0auAFcTx+UnQ+E/VyEVM1Wg9kiZD2msg6TWQ9VtoDjrI+q1k/RZaEl0kvSy+BAgyYfQ1g/eqo64Rr04AYqOPQ49JI7fV7wEqtsRYOEiuMkA+HGE0HCRX7qMQjVKMxilGY5RtMT6PEFUlFoe3FAYLMibIPoStBu/HkVZeBt5oyqZHR8eLeCZAgDZZwdHodTzxnSDMAk4AzoGW7jsBiUdmVYJkC5XScIeIuRT0BlVuAr0auETRxunn185TFBHB4JHw0mS8ZpoTnbQlltGaWExrcglZv5mU10DGayLpZarGHY/6tXfjhO9O9vrU355opFL399TX4jmG2FsItUIxGiUfjVKMxhitDDJcPsZgqYfBcg+jlUEKUY6KLU14DiLCKTwGCwwCu4EXBXnBE/8lEXNouHR8rCnRgW8CQi1i1TohmEGcAJwhzVs3A4IxHorSlGiXkXL/CuAWVb0d9J3ApUDL9HO16lKLCIGkSHoZGoN22hJLaEsupSO5gtbEEpoTXaS8LAmTribPJg2w9vcsJvxOE0Hq/q49YaghFVtgPBxhuNLLYKmH/tIhhkpHGSofZTwcoWTzhLYSv8vJPYVIkF6Q3UbMM8BjCZN6uRCNjdQO8BrTRLk8uWv+eY4/h4WNE4DToG37B6nFw1aVioSkSHYo9kar9m5F30ccy/v1500YPIJvkjQGbXQkV7A8cwWL02toTSwm67eQ8rJ4Vdc9Ps/OEyM/OyalYfJ5KlqiEI4xFg4wUDrC4fwujhbeYKB0mEI4SqRhfPxJBEGQnIh0W7WPAo8D3cCYbwIiG4LEn5PzDM4cJwCnoKP7HooU8AlAlUhDfJNoVOwmVb0b2KJwJWi6dk5s8PEo7ZuArN9CR3IlSzPrWZa+jEXpS2gM2gkkhdRCh2rMfzFQLwyWiGI0zkjlOEfze+gp7OFwfhfD5V6K0RhWo4mE5jSGged9Ce5H+GFkw71AJeGlyYcjGAKMcWJwujgBmEbbtruQ8RFsQ3Ns9BIkI40uAzaD3qPoNUxx7xWrigikvSbak8tYnrmcpZn1LE6toSWxiIRJIZiqqduzu7ELEpn4YwnJh6MMlns4mt/DofxOeov7GS4foxwVTuYZqCBHFH0G5OGEST7Wmlx0qL/YQ6hlBCG3yYnA2+EEoEpr9wfiT0MhjA2/xWp0O/AJRd8DLKo/XrGoQtJL05VaxZrG61jTcC2dqZWkvAYMnjP4M0QmwgYh1DL5KMexwl5ezz3LG6Mvkiv3E2kFETNdDCLB7AJ91DPB18u28FIgyQoCjXYVI7LXeQSn4KIWgObuzQheze4ph0WSfnqVqr1H0Y8rej1103W1mD4wSVoTi1nd+A7WN17PkvQ6sn7zhFt/sbj0s00sB4aICkOlYxwcf5W9Yy9xeHwnI5W+apgwXQykH/RxI94/GDFPRjYcNuLhmwDBcPzq78z1Y80rLkoBaO7ewvCGR2jf/sG4ft0L/CiqbLTYjwnyU4quZ6IgJ3bxPfFoSnSyMnsV6xtvYEX2CpqCDgx+NWnnjH42EWJDD7XMUPkYr+eeYU/uBXqL+ylEo4BOyRcIUgCeV/QffAkeHBzfe7ApswpPPEKtYEScV8BFJgAd3fdQIc42q1o88Rojjd4N+gmFO0En3PxaQi/lZVieuYLLm29idcM7aE0sxpeEM/o5pGboJTvO8eKbvDH6IrtGfkJ/6TChjY277p+2FczroPcr+s203/BaOSpVfONhxKMQjZHbePFOJV4UAtC27S5CifDxCTXEE6/JavQR4NOK3gRka8fWYvYGv41LG69lQ8vtrMxeScpkqzl7F9PPH2K/QFFylX72jL7AjuEnOZLfTSnKn6zG4Jgn/sMi5q+TXuKZfGU8tHHJJaPXXJzewAUvAK3ddwOWSCMCSWQjover2s8oegfxslkAbOwR0JZcxuVNN3FVy210pVbhSxKLZaHOyV8s1JKHxWiMQ/lX2T70BHvHXmE8HKr+fkp40A/yLcX+DxvKy8ZXFQFVLrqZgwtSAJq742q92j8K33hBOSq/T5BfVvR2IBMfGcf3CZNiaWYdV7XcxrrG62lJLKpO27nRfqFRm0moaJne4n52Dv+YXbmnGSj1oNWkYR09wN8Df2XU3+V5Bt8EeJKg58qvz/WjnKfP6wKjo/seECHUCoIGityo6C+o2g9TN3+vakl5DVU3/71c0rCRtNfExVSYc6FTE/Hh8jF2555n+/AP6MnvwRJNLzDaL2K+6kvwdwPje/e1ZVdT1gKCueAbmlwwAtC5/cOMRkOkTQMtXrsMRwObrEZfUPgXoG2146xaApNgTeM7eVf7h1jVcDUJSbuk3gVMzSsYDQd5beTHvDzwEL3F/Sh2ihAYMbsM3lcV/ZrAwbC6IvJCDgsuCAFo674bRQm1gi/BMsX+sqr+rKJLa8fY6vz9iuyVXNt2J+uaridtGrFE53JpxwKiFhKOVI6zfegJtg49ykDpyHQhUJDtAv+vwN9btOh7CawNGd74yFw/wix8JguYpq3vJ51ophSO44lnQlvZAvyuojfWjonbbfksyazl+vYPs77pBjJeoyvYuYipzQwMlI6wbehxtg//gKHysSm/A4qC/CPwR6q6y5h4Vebwxofn+vZn+LNYgLRtu6vasUaqlWAsUvTXFP0M0Aq19taGpem1XNO2hSuab6bBb8fF+I4atRxBX/Egrww+wo7hJxkNB6YtcZadAv9ZRL6hULzxyn/DSzu/Rv+G78317c/QZ7DAaNt2FxUJ8dTgqTGhRHco+jvArbVjrFqaEx28s+1urm37AI1BB87wHadCMFgijhbe4Pn+f+K1kR9RscX6sKAgmK8ZMX8UafhGvLhL6NvwT3N96zPw7AuIpm1b4j50KojQpapfUPRzQDvEJm7wWNN4Lbd2fYIV2Svrlt06HG+NwVC2RXaMPMVPjn+D/tLBKd6AIN2I/OeEpO4PtVLJMUSWRnIbH53rWz9rFoQANHVvwcePC3JERK19r6JfJF6lJxCP+k1BOzd0fIRr2+8m6zVVC3gcjjMhnjE4XjrAj3v/kZ0jP6aipXpvYEyQvzPi/TGwzxKh2AVbTjzvBaCpezMFxmmgGZAGJfq8VfsbQCfURn3D6oZN3Lbok6zMXuVGfcc5IxjKtsCO4Sf5yfFvMFA+PL2acKuI+Y9lKT2Y0ITGuyRVFpw3MK8FoKW6Rt9TD4tdZzX6T4p+jGrrLauWhqCV69s/zHXtH6TBb3GjvmMGiQOA3uJ+fnT8H9k18pNqs5EJIRgUMX9sxPsyqrlRM0jaNiyo4qF5KQCN3XeQII0lwvM8E0bh3VbtH4BugskM/yUNG7it62dY1bARU+2443DMNIKhZPN0Dz3O0333M1TqqS8pjgT5phHvi4LZrRL3gBzc8OBc3/ZpPts8o7l7C57xUCsYkebQVj6v8Bu1aj7FkjQZ3tl+Nzd3foxGv9WN+o5Zp1Yf0FPYwxPH/hd7R1/CYideF6RbRP59U7L9wbHSsHriU9Txee8NeOf+FjNHW/cH4w4wNkKEK6xGf1rN8mchNv725HI2L/0Fbuj4KVJexo36jvNKU9DBmqZrAegrHpjoP0jcMu4DpTDvecbfatWWQUl9dg2lr+yd69s+JfPGA2ja9n6MeKRMo1eIcncDf6joBphM9K1tvI7bF3+aJel1bqWeY84QhEhDXhv5MU/2/h0DpSkJwlCQb4mY/xRp9JpIXH8yXz2BeSEATds2A2AJA4/gVxT+A2i1os+SMg1c1/5Bbur8abJ+izN+x7xAEI4W9vKDY397QkgA8hroFwR5QiXeLm0+zhDMuQA0dW8hbrYhSVR/Hfgd4r3tUbV0pFby3kWf4ormWyZ2lHU45guCYTwc5pm++3lh4PuU7Hi9N7AX+AI2ehgv3jNmvonAnApA09b3gwiIpFH998BvAslYEAzrmt7F+xZ9msXptW7Ud8xbaiHBzpGf8GTv/65WEE6IwGHg81j7TxgDqvNqO7M5SwK2b/8QIoJqlAX+A3XGL+Jxbdud3LX0XtqSS53xO+Y9IoZFqdUsy15Gb3E/uUpfLRxoAm5F5ECmeekurZRp/MIGxv/bzrm+5fi+z/cFW7vjffYAPBNky1H+94BfBYKa8b+r/UO8b/GnSRqX5XcsLATD8eIBvn/kSxwc21FfL3BUkF8bOfDo1zvWfITIhgxtfGCub/fEjddmH61u92CaQlv6Q+DXgEBRPAm4of0jzvgdCxbF0pW6hA8t/1UubXxH/b/hJcCXWlff/cmkXYbB0LX9I3N9u+c3BGjpvqtq/F5zqJU/VuxnAU9RfAm4ufOjvHfRp0iYtDN+xwJGyfqtrMxexUDpCIPlI7VwoEHR90YyMnBHy8e37i+9RvredRTu2z1nd3reBKA21edJ0BxR+WPF/gJgFCWQJLd0fZRbuz5BYJLO+B0XAEraa2JF9goGSz0MTIpAGvS2/aXX+i5ruvWVvuJ+Ep+9hNJX9s3JXZ4XAWjq3oKIwYjJWqI/sBp9FhBFCUySWxf9K97d9XFn/I4LjFgEVjVcxVD5KP2lwzURSIHe0l8+eChIN+yIwhLJz62ldN/5rxicdQFo2vb++BshrWq/qOivUHX7EybFbV0/w82dP13dbssZv+NCQ0l5jazMXslI5Tj9pYNUc+8Zxd4chcV9aqNdYoTEvasp37f/vN7drApAR/eHQCCkEhjMvwN+C0jEbn+CWxd9gls6P4YvgTN+xwXMpAgMlnvqPYFG4CYR86oviX2gZO+9jMJ9e87bnc2aAHRu/wgikPUavYqt/Cpx374UdQm/W7o+7ozfcZGgpLwGlmcuZ6B0iMFyT00EmoGbELaiejBtMmQ+dxnj9+06L3c1K9OAnds/jAD3tHyW0WjkF0F/lzj5ganO89/a9QkC5/Y7LiIUS2tiCXct/RyrslfXF7itVdX7PPGvy9sxfm3NV1j02kfPyz3NuAfQ2H0Hngno63uAN83Ap6xG/4+iLfFvhWvbPsAdS/6Nm+pzXKQoGb+ZpZl19ORfr2tDrl0K13riP/NU/zeODxd60L88Out3M6OVgE3dW1ATEdgUluiDqvavFF0cP7Zydct7uXvZ58h4Tc74HRc1guFIYRffPfSn9BYOYKoVgyLmKUF+DnhTMAxtnN3OQjMaAvgE+DaBYi9XtX80afyWy5tu4s6lv0TGa3bG77joUSzL0pdz97LP01633kXVvkfR3/XETwvQsf1Ds3ofMxYCtHbfVXuIJlX754q+N35QZU3DO7l72edpDrrcwh6HYwKlNbGY1uRSDo6/StGO18KBq1Rt33D5wPMNfifpe9eRn6VqwRnxAJq7NyMISxIrxWr0WUU/Ej+epSO5nM1Lf5G2xBJn/A7HNBRlfeP1vGfRJwlMkupCuQTw2y3JVbcV7DgD4THatt01K9efEQEY00EU6Cm9uQXk/wJ8RUmZLO9d9LMsTq12jTsdjlOgwIbW93FN65aJ4FjRpar6+x7ekiavjUhmx37OWQDat99Dk3Sh2JWK/QPQToibJFzbfhdXNN/iYn6H4y2pFsZ1/StWZa/GajUfgN6m8NsiXsJg6Nz+4Rm/8jkJQNv2u1EsnvhpVftF4Lr4xi2XNryDWzo/hif+HHygDsfCQlGag05uX/xpmoL2iUFTsT+v2E/kozECSdLWffeMXvesBaB5+2Y8EzA4uIOKln9e0U9Vb5iWYBHvW/JzZP1WN/o7HKeJxbIqu4FbuuLy+CoZVL+Y9jLXjEUjhFqZ0WuetQBEUUQ5LNLSeuUNqP7fVNt5BZLi1kWfYFn6Mpf0czjOEKkWy13Vctvk1CC6RlV/X6BZENq2z5wXcFYC0Lnjw/gmwIhkFf0tRZfXbv+ats1sbL3DjfsOx1kQr5LNcFvXv2Zxam29CHwA5FOhhjN6vbMSgHSQpRjmsWp/WtV+EOIW3kvT6+N1/ZICJwEOx1lR2wHr9sU/S8prrIXRvqK/4ot/WWRD2rffMyPXOmMB6Nj+YXKlQZJ+ZiXwf1J1/ZNehpu7PkpzsMi5/g7HOaJY1jZex8aW2+tfXQ/yy2k/64PS3L35nK9zRgLQ2H0HSkRT0G5U9QuKXgOgqlzefAvrm25wxu9wzBCeBFzf8RE6kivq7Eo/VQzzm61aEpI55wKhMxKAlGkk0ojhcv9NwM9BHLO0JBZxQ8dPEUhyrj8zh+OCoVZJe33Hh/CqswKKNiv6G0ZMe6RlIjm3nMBpC0Bz92YireCboFHgt0C7IM5avrP9bpak17jR3+GYBTa03M7qhk31BUK3Rzb82UgtlpDG7jvO+r3PyAOINKQclT4eZyTBqmVF9kquadtStymiw+GYKRQl4zVxY8e/JOtPrKQ1FvsFEa72NIFPcNbvf1oC0LRtM54k8MRbLXHiLxG3OMpyc+dP0+R3uIIfh2OWsFgubbiGja1TRvo1qvorxngBcNYJwdMSABEIo5DQVj6t6FUQK9MVze9mTeN1WKK5/owcjgsaIz7vav8gncmVdbUB/LRVe0O8le7Zldy/rQA0bduMKiB2DVAt91VaEou5sdMl/hyO80FcG7CCd3V8qM7YtU3RX/DEC8627uZtBUCEWABi418LcR+xDS23syi12iX+HI7zhnJF8y1xwr2WEFT9UKTRjQpnVSL8lgLQ3B2P/iKsZWL0jzubbmx9X/0e6A6HY5ZRlEa/nWvatmBkihfw8554QU0UzoRTWnAtqVAd/T/JxOgvXNXynmnFCQ6H4/ygXN5888m8gBvOxgt4yyG8OvrXxf7x6L+h9XY3+jscc8CkF7B5uhfwC57xAj3DEuG3FQDqYn+qo399JtLhcJxv4tL7E7wAG92gqpgz6PV7UgHo2H4PnBD7K21u9Hc45py39ALECxA57TUCJ7XkQjRGpBZBPs602N+N/g7HfOCkXsA9kUbXqSp6mmP0SQ/L+M1k/IZm4O74Ukpz0MWGFjf6OxzzgSlegJnwAtpV7Yfy0fhE/P52nGDNjVs3E9oyZVu6AdgE8XLftU3X0ZFymX+HY/6grG+6kY7k8vrqwA9kTKZLz1YALBH5MCdWo3+paEPc7CPN5U034Z1luaHD4Zh5FKUp6GB1wzvqBny9AuEmpZrLexumCEBj9x2kvAwNQesyQd4D8ejfnlzOkvRaN/o7HPMMg2Fd47tIeRmq5cApVb0n42eM1bdfozNFACTyCW0FRW8E1sQvwuqGTWR8t6mnwzHfUJSlmfV0pVZjtbaXAO8pRPmVp7Mb1xQBUGNRNBFp+FFFg3gtcgtXNr/bJf8cjnlIrV/A2qbrEKn15NBLVfW9qkpH91vvLjzVAwDArle1t0G1029mLV2p1W70dzjmMWsbr6tvGOIBH/ZNkIwI37ImYEIAatl/I/57gSUAIoZLG64ladK4Nt8Ox/xEsXQlV7Esc/lkTQB6c2jDy61aUsmmU547IQAiEJhUSlW3VN+ARr+N1Q2bnOk7HPOchEmxrvFd9XtxLgJujzQkV+o95XlTcwDYpYq9BmL3f3n2CjpTrvLP4ZjvKHGyvrFuY1Hg5rSX8eONek6Ogdj9r3I10AVgxLA8czm+6/jjcMx74pqAzniZ/kRRgF4dadQlb7E4yEDs/ld5J5AECEyaJel1rtuvw7EgUBImxdLM+gmLVXSFxa63hLR033nSs+pDgCRwQ3yipTnonFJi6HA45jeCYWlmPb6Z8NobQN9p1WJOMY1f/+py4AqIq/8WpVfXTys4HI55jqJ0JleS9Vsm7FaVG1Jexj+VFZvGbe+vfX8lceYQEcPS9Hp8Scz1MzkcjtOk5rl3plYy2R9QrwptpetUobwxmJpa3EBtp1+TZmlm3Vw/j8PhOEMCk2Rpev1EVaDCKou9zBLRsu0DJxxvFItAGrg+PiHe7LM9ucy5/w7HAiPOA6yr269Ds6DvUlUsJ24kanxJ4EliqSDrII7/O1OryHgtTgAcjgWGonSlVtEQtE3mAeDabNAaJLzsCccbRVHsMqrz/4KwOHUpvri1/w7HQkOxNPhttCYWT+YBlDWlcCxrbeWE402kIap2taIpAM8ENCcWgZv/dzgWJIFJ0Bx0Tfys2K5QK52RniQEAEBkHVVvIGFStCQW4Rb/OBwLE8GjLbl0IhEoSLsRb4mREysCjRHPV7Wr4h+VtNc4vZ7Y4XAsIAShNbEETwIAFE1HGq6O9MSlwcaI11ifAGwKOkl5Dc78HY4Fi9KS6CJh0rWB3BjMesVSpjzlSBPacruinbUXmhNdbv2/w7GAUZTGoJ2010jNji12lcH3vGkLg4wn/qUg7QAiQntymWv/5XAsYBRIeQ00JzonVgYKss6I1zg9D2AiDVeDNgAYPFoTS9wKQIdjQaMEJkVT0FH3inZZDZumdwo2BrMe8BQl6WVoDjpx7r/DsbAxeLQllyEy4c23Cmbl9MHdGPEmJgwDkyTtNznzdzgWOILQ4LdOePOCpDzxm820Aj8/0miiY6ARn8AkcR6Aw7HwiZP5QtWefUt0QnsvX7HxZCGKweDJ6e8t7nA45i++SSAIcbm/epGGwfRjDDCxQiAwKQxOAByOC4F4od8Ue26YfsyEAKjGrYWNWwTkcFwQ+JKo2vNESH9SAWis/RCYFEaMywA4HAseJfBS+BLU2bM0TnYKijGCaZ44wSSJCwWcBDgcCxklntXzzGTYb8RrHQsHpxxnRCY9gIRJYXAhgMOx8IlX9npTQgBt0fKBKUcZqzZd+yFh0m4WwOG4QPAkoL7016pN8+bQlGMMyIS/b7FuGbDDcYEioKSnvmYEydd+CG2Z6UkCh8OxEBHKtkhkK9S6exnxx2ifulOwAUZqP5RtnugknUMdDsfCI7Ql6tuAqUa5RMPVU44xiq0KQKwY8WohtxrQ4VjICFCZJgAWO5QyUzsDG2C8dkI5KhBp6Mzf4VjwCKGWp9vz6PSjDDBWPZ6KuhyAw3GhULZFIp3MAXAKASjUfghtGUt0eu/ucDjmNZGtMK0BSH76McYTrxh/K1gNCU+yeYDD4Vh4VLRcXwYceeKH01uC+SDjtR8iDanYInVriB0OxwKlbPPU7Fig4omfn17n41uNDgMqIGVbZDwcqa4hdjgcCxVFyZX7iTf/NSiaD215cPpxBngNCONpwALDld65vneHw3GOWEIGy0cnugIDw4rtme4BGJDDVLODimWodBTFzQQ4HAsVQShFBXLl4zDZE/Cwb5IjvpnaFMgA+0D6IN4ZaLDc42YCHI4FjVCMxshV+if2B1R0X5nRsbIWpxxpPPGHBXprJ46U+yhFebc3gMOxQBEgV+mjaMcnrNiI9yaRr2bapj+mQnFM0Tcg3hlotNJPIRrFlQM7HAsVYbh8nHJUoGrHkdXoNRHDyMbHphxpULFGvANUD51wHeb6GRwOx1mh2DiUrxYBCTLuiX/YO0m/TyMIVqPdTMwElBipSx44HI6FhcUyWDoy0dtD0T6rUc/0bcEAjC8JfEkcFKQAYDVkqHzMNQZxOBYk8XT+SKVv8hUxxwOTHPDMCdsCYBBAOAIchbiA4GjhDUItzfWTOByOM0QQRisDDJWOTu4LqLozMKnxk43pRtViML0guyBOBPYVDzJaGXQzAQ7HAkMQegv7yEe5mv2qoi+Nh8O2Eo6ccLxRlLItlkR4Ln4Dw2g4QH/pEDJtysDhcMxvLBFHCrsJbbn2Ug54GSDwGk843ihaNXR5gepywYot0ZPf4/IADseCIo7/e/J7qEvi7wX2AAxueuiEM8zIxkfwxMNgXhfkCICq5XB+F5VpVUMOh2P+IgjD5V4GS0cmKgCBbaoMneocA/G8oRFzFORVABHDQOlQNQ/gwgCHYyEgCMeLB8hHI/X5u+dEsHKKdJ4B8MSnGBUqTOQB4kxinAdwiUCHYyFgiTicf72+qc8Q8NJbnRMP7yL4xkeQl6nlAbRET/51lwdwOBYA8QrAcY4WpsT/+4EDwAklwDUMgI1CDB6C7BSkB+Ltwg/nd1W7ijgvwOGY3wiD5aPT4/9uQQbMW0TxBiazg0bMMapTBiJCT34Px4sHqtVCDodj/qLszj3HWDhcDdvFGvGeMuLpyMipz5rUBoHQVirAA0AkCPkoxxujL7sgwOGYxwhCIRpj39grdR2A9KBgfqxAY+Opz50QgMENDyJiMGKeEmQvxA1C3hh9YXpW0eFwzCMEw/Higdhbn3T/n67Y4oFIK+Q2PXbKc6dGB6oE6h8EfgBgJJ5W6MnvdtOBDsc8xRKxO/ccxWiM2B+Qoif+txNeOkTfeuCeYtWKUqKsgnwPyFPtLbY79xzWbRrqcMw7BCFX6Wd37rnJ10R2+SbxlMEwes1jb3n+FAEY2fQoIgYReV6QnfGbwb6xrYyU+1wY4HDMMwTDkfzrDJWPTnjpqvqDvn3f7fNN4m3PP8GvN2LIh2P9IA/XLjBUPsrB/GsuDHA45hkRIXtHX6JiJ5bvjyv6cPOqLZPLgd+CE44QDCkvC+iDxJVEhLbM7tyzVFyPAIdj3iAYBks97Bt7ZcLYjZjnfUk8J2I4euU33vY9ThCAgQ3fx4hgxOsW5EWI1wbsG32Fw/ldGOcFOBzzBGVX7mmGy7314fkDxWgs155afFrvcFJr9sQn1HBMRL5JtSZgPBzhlcGHqWj5tN7Y4XDMHoIwVD7G9qEf1G/kc0RVHwlMktHy0Gm9z0kFwGLxxUcw36muD0BE2JN7nsP5nc4LcDjmAa+N/Ii+4sH63NzX1VReVVGOX/3d03qPk1ry4IYHMSSINDouIn/NhBeQ45XBR5wX4HDMIbXRv3vo8fpdvI4Af4v19Uzm6k45lEcU8cQgmG9P9QJecLkAh2OOOcno/w3PY7uc4Uz9Ka14eOMjYEIijXqnegEuF+BwzBXx6N87ffTvAf4miuJlO6da+nsy3nIYt1acF+BwzDNeG/nhCbF/bfQ/E+OHtxGAkY2PgajzAhyOecBbxP5/E0V1CwHPgLcdwq3aU3gBz3No/FXnBTgc5wlF2Tb0zxwvvjkl9jcmHv3fatXfqXhb6x3Z+Bgq0QleQD7M8XTf/RSiUbdGwOGYZWo1/y8PPlzXpk8OA39j7dmN/nAaAgAg6mHEAPJNQZ6GanXg2Cu8OvLDuf5sHI4LHKFiizzb/x1ydYvyROSrl7det903wVmN/nCaAjC08WFQiDTsB/4L8W4jRFrh2b5v01867BYKORyzhCDszP2E13PPTPT7E+QlVXvf60MvKefQs+u0rdY3AYEkCCTxiGC+Ht+Eoa90iBcGvkekrl+AwzHTCMJI5TjP9n2bSlSk2qC3APKnka0ciSqVc7K90xaA/g3fA5SQSsWI/BnxlkMAbB96ggPj21xC0OGYYRTlpYEHOVp4Y2LFnyDftUTf8k0Ck0ic8dRfPWdksYMbH0IUItHXjJj/St204LN93yLvEoIOx4wRJ/528crQo/X7c/QAfwYUFSW38ZFzusYZD9kKGBUE76uCPAFxE5F9Y1vZPvwD3B4CDse5Iwglm+fpvvsZLfdPbPVtxHwlQcPzBjnrxF89ZywAw5seQSXCEg0BfwIyDLWE4HdiV8WFAg7HObNj+Al2556v7+zzvKr+VYnRGWvVf1aW6lkfgyHwkv8s8DWodicpH+GJ3v9FPsq5UMDhOEsMhkP5nfzo+D8STlbb5j3x/kSQo2PD4YyM/vG1zoLBTQ+hWCpROSSOR7ohFoE3ci/wfP93sZNNChwOx2kiCLlwgCeOfZWh0rGJgdSI+XvgexZLY6s/Y9c7a1/dqGGkvAuQN4yY/yjVUMBiea7/u+zOPedCAYfjDIk05Nm+b7N/bGu1+A4EeR7kD63aIqrnlPWfzllb6OCmh2hLXIlnPDJB4wPAlwAVhEKY48ljf8eAKxByOE4bwfDayI95ceCB+hi/F5H/EGpl/3g0ipqZ3ajvnKwz3lRUKFTGrRH/zwX5PsRlwseK+3iq9/+jZPMuH+BwvA2C4VjxDZ7q/d+U7HjNZiJB/nRk8PF/Tpo0rUEnoxsfn9HrnvPwPLjhAQQPYFAwXxTkjfiBhFdHfsjLAw/Wz2E6HI5pxJt75niq92v0lw5NeM2C3C+Yr7S0vh+Avg3/NOPX9mbiTfx7V2AwWKJjRsywoluAhMXSW9zP4vSltCeWOSFwOE5AUCKe7vsmLw/EHnX19R2C3qvYnkhDRjadW8HPqZiRAH104+OoWjzx8Un8vSB/GT+aMBYO8mjP/+BQfqfLBzgc01AsLw08xLN9366bOZNhEX7Poq+3mDYSkpy168+IBwBQ/MpeMveuR1FrjNmqqtcCqwVhtDJEb3E/y7NX0OC3cS6rlxyOC4ntQ0/w2NH/SdGO1eJ+K2L+uMlv/4pitUSJwY0Pzdr1Z0wAAIJ7V5MghYqOA6+CvhvoFBFGK/30lw6xouFKMl4zTgQcFzOCsGvkaR7uuY98NDLhHRsxXxMxv1PRUsFgGNjwwKzex4wKQOm+vZh7l5E0GUo2f9STxKvAraBtIsJw5RiDpSOsathAymvAiYDjYkQw7B17mQeP/DdyYf+k8eN910jwK1aj/kgjhmdx5K8xowIAUL5vP5l715OUDAUdfdOXYA/oe4AmQRgs95Cr9LGqYQNJk8GJgONiQjC8Ob6d7x/5EkPlnvqR/zFP/M9ZoiMWZXSGSn3fjhkXAID8fa+T/tx6EpJkLBp5w5fgIPAeoEEQ+kuHGKsMsrLhahImdV4e1OGYawTD4fxOHjjyF/SVpjT2/LGI+Yxi96lCbtOj5+2eZi0t37fhu0RaIe1lSWvz/cBvUt1uHGD78BM8fvRvKERjrlDIccFTK/R58MiX6S3sqzf+l4EvoOzxNIF3nmfKZsUDqFG4bw/BvZcQSgk8bzuqI8BtQBKU3sJ+8tEIK7JXkjBpXDjguBARDD2F3Xz/yJfoKeyuX967A/glVF+2nhJRZuQ8jv4wywIAUL5vH8l712JUSPkNr1iNChqLQACWY4V95KMRVmavcCLguOAQDEcKr/PA4S/Rk99d39brDU+CXxSRZxRFEEY3/vN5v79ZFwCIZwdS967FaqSBpF4CG4HeAvgAxwr7GK0MsiJ7pUsMOi4YBMOh/Gt8//CXOFqc0tNvnyf+Zy3hkx4+Vmduff+Zcl4EAKB43xuk710PqE2Z7LMh5bLCzUAAcLy4n7HKICuyVzkRcCx4BMPB8R08cOQv4pi/buQX8T5T0fLjKdOAxc5ame/pcN4EAKB43x4aPncFERUbmNSzSjSq2JuBJMDx4gGGy8dYkb3S1Qk4FixCvGnO9498Kc72Txr/q54JfskSPpmoDnKDG78/p/d6XgUAqlOE964nIrQpv/HFii0MA7cAKYC+0kEGy0dZmb2ClNeIEwHHQkIQ9o69zAOH/yLuhzGZ8OsW5DOVqPCTTNBKaCtzbvwwBwIAULhvN+nPradiC2pt9JKI9AHvBtK1OoG+4psszawj67fiRMAx3xEERdk58hMeOvJlhipH643/ZeAXRczzST+LMT79V393rm8ZmCMBgHiKMPGZSxBjFN/firX91InAYPkoB8d30OC30p5a5jYdccxbBEPRjvNM37f4wbGvMhoO1M/zvwB8BngJlMhWGNww9yN/jTkTAIDSV/aR/NxaUAXP24rqQWIRaKgtJd439jJWIxalVxOYFM4bcMwn4u3x3uTRnr/kpcEHKdvClAo/4BeBbkz82lxl+0/FnAoAxFOEyXvXgFoSNrsjksp+Qa4F2gShomUOjr/KQPkwXalVNLiQwDEPqLn8r+ee5cEjX2b/+NaJ14l7Yz4kIl8QZCeeggq5jee3yOd0mHMBgFgEEvdeCiZi3OZ2Jk3qKZCloOsFEVD6Sm/y5vh2GoM22pMuJHDMHYKhEI3xTN/9/ODY3zJcPlYf748K5s8Q85tWo0OLF7cwOlaYkyKf02FeCADEFYON915Fg9dCqOVeI+YR0BBkE5CK9yAcYu/oy0Qasih9qQsJHOcdwXC8eIBHjv53Xhp4iLIW66f5dgvy64FJf1mJxi2W0lh03st7z4R5IwAQTxF69y5HxGAwxcag9amyFvcIbAQ6pocEnakV1ZDALSZyzC6CwWrI67lneODIf+XN8e7q69UuPsiDIuazZS39wBPPCgaVcF4bf3z/85DG7jtISRZLRDkq4Rn/alX7h4reQ3UFo2JpTy7n5s6PsqHldhImjbrdiByzgMEwVOnl2b5vs3XoUYrRWF2iT3ICf+FJ8GeKHfDEw2o0q228ZpJ5KQA1WrZ/IN4dxYKItIa28usKvwzaDLEI+JLkqpZbuaXzY3SlLqkGBC4scJw7ghBpxBujL/LD41/jSP71iderX3eKyO+kvOx3ylEx8ggoMjbjvftn9xnnOY3dd5CigYgKnud7laj8U6r29xS9Oj5CUZSO5Ere3fVxrmy+1XkDjnPGYBip9PFc/3d4afBhiuFofaIvBPmeJ94XFbvDiAcIg7Pcv282mPcCUKNt+92xqatFMGut2t9S7CeBDMTeQCAprmq5jXd3fZyO5EonAo4zRhAsEXtHX+GHvV/jcP41FOqb1hwW5E9EzF8LkkuYFJWoWN0la+GxYAQAoGXbnWRMAwXNI0jSEn1MVX9b0SvjI2JvoCt1Ce/u/DhXttxKIEm3U7HjNBAMQq7Sz3MD/8TLAw+RD0fqR/1IkAdBfn88yr3Q4LcAgiWcl/P7p//UC4y2bXcRShTXASiImMuthr+t6MepLihSLAmT4Yrmm7mu/R6WZdZj8J1H4DgJgsFQsuPsGX2RZ/q+xZH8LmpNOqr0CPJnIuYvVe1I7PLD0AJJ9L310y9Qmrq3ULTjNJhmLDataj+h8O9A18dHKFaVxqCVq1pu4x1tH6ArdQkGzwmBA6Bq+AX2jb3CK4MPs39sG6WoMLEtN/H03qPA7+fJP52VLKJCJHZBj/r1LFgBqNHWfTeKJdIIwVwF+tuKfgxIANX9CJWWYBFXt7yXTW2b6UyuYPJ3josNwRBqmcP5nbzQ/332jD5fNXyByQx/r4h8SVXvU3QokASKMrjxwbm+/Rn+LC4AmrdtISzn8RMZRExG1f4M8HmFTaDVuoHY2NsSS7mmbTMbW++gJVhELW/guPCReANbDo2/xksDD7Jn9AUKYQ6pM3xgTJBHjHh//v5VH/3Rowf+AUUx4jG8ce4698zeZ3KB0LT1/XheAtTGiwuNt1zh45GG/1bVXl07TrEIhs7UKt7RdidXNd9GU9Ax8TvHhUac3IuIOF7cz9bBx9gx/CSjlSFEpD7OLwnyI0G+HJjEwxUtF0UMViNGLhB3/+SfzgVG6/a7iGyFwCQZr+TIBE2rIlv5pKL/FlhbO06xGDy60qu5qvlWLmu6iY7UCjw8bDVscCxcYtM2lGyensJuXh3+IbtzzzFSOT7x2yqRIE+JyH8XMQ+rtTkjHiEhvnoLdnrv9D+nC5SW7jsJTILQRqiNsGLXAf8H8ElgRe04VQsitCQWsa7xeq5uuY0l6XUkTboaHDghWEjUSnTHwyH2jW1lx/CTHBzfQT4cnT7iR4JsBf6nwj8KDMbZfYOlzMjG+bVuf/Y+rwucpu4tIALWkh+1ZBu9TSLyS6r6UUW7asfFRUZKxm/kkuxGNrTezqrsRrJ+S/X3LjyYzwgGxTJY6mF37jl2jDxFb2EfFVuebviAvGqQ+4x49xdt/lgtwecZn6ENF/aIf+LndpHQvO1OVBURyAZNfikqXhdp+Gmr0d3Aqskj4+nDwCRZnL6Uq1vew/qmG2lNLJ6YQnRewfyg5uaXtUhvYR+vjvyQ10eeYah8LK4YlSk9IyqCbAO+KSJfjzTc70uSjGQoapGBedCgc24+w4uI5u7NEz0EImuxGhklWmfE+xeq+jFFN1LdrATi8MCIR2tiCeuarmdN47UsSa8l67diEJcrmANqRh8RMlI+zsHxHezKPcPB8VcZD4eYFt8D5AT5kYh8DZXHK1rqDUwCqf5vHtq48Or3Z5KLSgDqady6Gak+fTHMkwkaF1mNNouYf62q7wZtrB2rxDMLSS9Ne3IZ65tuiJOGyeXE/d1diDC7SFVwLWPhEEfyu9iTe4ED490Ml48R2goiZorhC3IYeFDRr/sSPBNplBeEjNdA2Rbpv0hH/OlctAJQo7l7M/EabrBqSXqphnJUvEnRTwjyAUWX1h9fSxpm/WYWp9ZwaeO1XNpwDZ2pVQSSrKYNnRicK1L9o0AxGuVoYS97R19i79hL9BUPUbElRCaTflUiQV4F7jfifSvwgp3FsBh54uHhUyK/oJbqng8uegGo0dr9AbJ+CyU7Xk0cGc9gNoS28mERuceq3US1uhCYWJloxJD1W7m04R2sbbqOpen1NAXtJEy6mphygnB6yMQfS0QxGmOgdJgDY928Mfoixwr7KNqx6pEn9IMcEORFkG8IPFyypSMpLwUiqFoUe9Fk9c8UJwDTaOregqiCGAJJMFYZJhM0LQ5t+SbgTkHeA6xRNKidUxMD3yTI+i10JleyNLOeFZkr6EitoDnoxJNEdURzScQYqRvlLUU7Tq7cR09hD4fzuzhW2MtA6QjFaBSrOqVMt8qYIN0gjwo8KCKv1tx8z/jxEl6rF/w8/rniBOAtaN/+QdJ+I+OVESIN6UgtlpHy0DKr0S2Rhh8j3tx0MXWf42TPAiHwUjT4rSxOX8rS9HqWZtbTmVxJxm8mkARUW0tfDOXIMpGci5+5bPPkKgP0FvdzOL+Lo/k9DJSOMB4OEWkYn3HC9B1lQXYDjwMPGPFerNjykC/VvG3cQJrhTQ/P9eMuGJwAnCadOz4E1RZRqkqklSSwVpD3iJi7VO0NinZOP29CEMSQMClagkV0plaxNLOejuRymhNdNAUdJEwaX4Kqe6sLtgipZuS1JTWWiIotUYzGGKn0MVQ+Rn/xIEfyr9NfOsRYOERoK4CekMirEoEcAp40Ig944j89UN7X0+yviFftiWLVufhnixOAM6Rp6/uZmD4AQluhMdGWKkeFDcDNir1ZVTcqugpITz8/nlFQjBg8CUh5DTQG7bQkFtGeXE57chkdyeU0+G1k/WZ8k8Tg1RlGTRYmv55PJu9j0sgBLBarISWbZzwcJlfpo694kIFSDwOlw4xW+hkNBynbIlbDak3GSQ0ekEFgL+iLgvmJiDxn8PZHGka+8fHUI9IQS8TQHG6tfSHgBOAc6NrxEZJelkI4GnsGWLJ+UzAe5hap6mWKvRF4J3CNIEsVTU5/D0VBJ0d7TwISJknGb6Ep6KA1sZjmxCIa/BayfguNQTtpv5GESZMwaQKTrG6SIqcwpomrTHw/iUz7Tk55tmKxainbAmVboBTlyUcj5Cr9FMJRcpV+hspHGan0kSv3U7RjhLaEVRvfm0x6BychJ8h+4BUReV4wLyq6x1MdCVGd6Lsf+Viv5Eb7GcQJwAzR3L2Zsi3Q4LVR0RKq1BJ+CU+8pYK3UbE3qdp3AZcp2gpkT/5uOlGaHBPHw74kCEwCXxKk/SYa/BbSXhMNQSvNQWdcoCQeRgy+JPHFxzMBviTwJMA3AYEk8YyPVUukFSINqdgSkYZEWqFiS4S2TKQhiqViS4yHwwyVj1GIRhkPhxkPhylF8WxJqPG58a0qp4jdpz4c5IBj1cq850Ge98TflfJSA6PhiPUlqD5/hFGPoWtcTD9bOAGYRRpe2YwxIGLw8BgLh8n6LQ2KXQxyKeilqvZy4HJgJbBY0QYgONV7To7lJwpEXbtqjPgYMRi8CVGIv/qY6vSk1ajqukdYjVC1E6611WjKNVVt3bVqV4m/vgUFQUaBg8AhRXcY8fYCu1XtmwLHI2xo8PCqbbYQwGXvzxtOAM4Tzd2bSdJMhfEpDvlw78M0L9qS9CTosBp1ga5T1ctALgddo2inIO2KpojLlM9wN6eTpRInhaOe0zDokxGCVATGFB0QTC/CayhvKLrTE++giDmGMlyO8pHvJevCnlhUcpvm5755FwNOAOaI5u7NWCwJSVG2RRImXZ1hiBAMab/JL0ajGVXbbsTrCLXSBLLcE29VpGE7sMiIWWnVthJvp95cFYnJLN3U/94Orfs68Z8gFsgrmhMkBzKg2AOC9IuYXqvRm0a84wZvONRyvy+JoUWN6ws9uVdVUTzxEfGIbBlEMKqAYchN1c0LnADMM5q630+kISnTSKRlUDDiE2oZqLnjEBgv4UsyU7bFrKIdvkkstRo2WrWGOIRoIs4xJIEmI16jwctaoqzVKCGYyIgpCVKw2JzVaBQoALWveUHKnvghIoOhlo/5BAOCKVYojqsS1TwGIx4eHhUt44mPMQGjhaM0JDqcKz/P+f8BNit5+f3wmm4AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjMtMDgtMjBUMDU6Mjk6NTQrMDA6MDDtgE2fAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIzLTA4LTIwVDA1OjI5OjU1KzAwOjAwOqr+lwAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyMy0wOC0yMFQwNToyOTo1NSswMDowMG2/30gAAAAASUVORK5CYII="
RSlib.doadmin()
a = os.path.join(os.path.expanduser("~"), 'AppData')
b = os.path.join(os.path.expanduser("~"), 'Desktop')
window = tk.Tk()
window.title("传说之下存档管理工具")
label = tk.Label(window, text="UT-toolkit", fg="black", font=("微软雅黑", 24, "bold"))
label.pack(side="top", pady=20)
label2 = tk.Label(window, text="作者:凌琳", fg="black", font=("微软雅黑", 10,))
label2.pack(side="top", pady=1)
button1 = tk.Button(window, text="导出/备份存档", width=15, font=("微软雅黑", 14), command=lambda: click_button_1_actions())
button1.pack(pady=10)
button2 = tk.Button(window, text="导入/恢复存档", width=15, font=("微软雅黑", 14), command=lambda: click_button_2_actions())
button2.pack(pady=10)
button3 = tk.Button(window, text="为坠落的人类命名", width=15, font=("微软雅黑", 14), command=lambda: click_button_4_actions())
button3.pack(pady=10)
button4 = tk.Button(window, text="真正的重置", width=15, font=("微软雅黑", 14), command=lambda: click_button_3_actions())
button4.pack(pady=10)
button5 = tk.Button(window, text="高级", width=15, font=("微软雅黑", 14), command=lambda: click_button_5_actions())
button5.pack(pady=10)
window.geometry("300x430")
icon_image = tk.PhotoImage(data=icon)
window.iconphoto(True, icon_image)
window.resizable(0, 0)
def click_button_1_actions():
    utfliepath = a + "/Local/UNDERTALE"
    if os.path.exists(utfliepath):
        RSlib.dozipfile(utfliepath)
        zipedutfliename = str(randint(1,10000))
        os.rename(a + "/Local/UNDERTALE.zip",a + "/Local/"+zipedutfliename+".utfile")
        shutil.move(a + "/Local/"+zipedutfliename+".utfile",tk.filedialog.askdirectory(title="选择一个保存位置"))
        messagebox.showinfo("提示","存档备份成功\n保存的文件名："+zipedutfliename+".utfile")
    else:
        messagebox.showwarning("提示","您似乎没有存档")
def click_button_2_actions():
    if RSlib.checktask("UNDERTALE.exe"):
        if tk.messagebox.askokcancel("提示","游戏似乎正在运行，要继续吗？"):
            flag2 = True
            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
            RSlib.dokilltask("UNDERTALE.exe")
        else:
            flag2 = False
    tk.messagebox.showwarning("警告","此操作会覆盖你的存档")
    if os.path.exists("./cache"):
        shutil.rmtree("./cache")
    utfliepath = a + "/Local/UNDERTALE"
    os.makedirs("./cache")
    if not os.path.exists(utfliepath):
        os.makedirs(utfliepath)
    doloadedutflie = tk.filedialog.askopenfilename(title="选择你的存档文件",filetypes=[('UT存档备份', '*.utfile'), ('UT存档zip备份', '*.zip')])
    loadedutflie = os.path.splitext(doloadedutflie)
    utflie = loadedutflie[0] + ".zip"
    os.rename(doloadedutflie,utflie)
    iszipfile = RSlib.unzip_file(utflie,"./cache")
    os.rename(utflie, doloadedutflie)
    if  iszipfile :
        flag = True
    else:
        flag = False
    checkfile1 = pathlib.Path("./cache/file0")
    checkfile2 = pathlib.Path("./cache/file9")
    if checkfile1.is_file() and checkfile2.is_file() and os.path.exists("./cache/undertale.ini"):
        flag1 = True
    else:
        flag1 = False
    if  flag and flag1:
        shutil.rmtree(utfliepath)
        shutil.copytree("./cache",utfliepath)
        shutil.rmtree("./cache")
        tk.messagebox.showinfo("提示","存档已覆盖")
    else:
        tk.messagebox.showwarning("提示","不是有效的存档文件")
    if flag2 :
        os.startfile(uttaskpath)
def click_button_3_actions():
    utfliepath = a + "/Local/UNDERTALE"
    if RSlib.checktask("UNDERTALE.exe"):
        if tk.messagebox.askokcancel("提示","游戏似乎正在运行，要继续吗？"):
            uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
            RSlib.dokilltask("UNDERTALE.exe")
            flag = True
        else:
            flag = False
    c = tk.messagebox.askokcancel("*","*你确定吗？你会抹除掉这个世界所有的痕迹")
    if c :
        c1 = tk.messagebox.askyesno("*","*你是否要抹除这个世界？")
        if c1:
            shutil.rmtree(utfliepath)
            tk.messagebox.showinfo("","*你扬了你的存档，这使你充满了决心")
            if flag :
                os.startfile(uttaskpath)
def click_button_4_actions():
    utfliepath = a + "/Local/UNDERTALE"
    if os.path.exists(utfliepath):
        if RSlib.checktask("UNDERTALE.exe"):
            if tk.messagebox.askokcancel("提示", "游戏似乎正在运行，要继续吗？"):
                flag = True
                uttaskpath = RSlib.gettaskpath("UNDERTALE.exe")
                RSlib.dokilltask("UNDERTALE.exe")
            else:
                flag = False
        tk.messagebox.showinfo("提示","修改非实时生效，需进入游戏再次存档即可")
        child_window = tk.Toplevel(window)
        child_window.title("请输入名称")
        child_window.resizable(0, 0)
        entry = tk.Entry(child_window)
        entry.pack(padx=20, pady=20, side=tk.LEFT)

        def replace_content():
            checkfile = pathlib.Path(utfliepath+"/file8")
            if checkfile.is_file():
                os.remove(utfliepath+"/file8")
            new_content = entry.get()
            try:
                with open(utfliepath+"/file0", "r") as file:
                    lines = file.readlines()
                lines[0] = new_content + '\n'
                with open(utfliepath+"/file0", "w") as file:
                    file.writelines(lines)
                with open(utfliepath + "/file9", "r") as file1:
                    lines = file1.readlines()
                lines[0] = new_content + '\n'
                with open(utfliepath + "/file9", "w") as file1:
                    file1.writelines(lines)
                iniline = f'Name="{new_content}"'
                RSlib.replace_line_in_file(utfliepath + "/undertale.ini", 5, iniline)
                tk.messagebox.showinfo("提示","成功修改")
                if flag:
                    print(1)
                    os.startfile(uttaskpath)
                child_window.destroy()
            except Exception as e:
                tk.messagebox.showinfo("提示","成功修改")
                if flag:
                    print(1)
                    os.startfile(uttaskpath)
                child_window.destroy()
        button = tk.Button(child_window, text="确定", command=replace_content)
        button.pack(padx=20, pady=20, side=tk.LEFT)
    else:
        messagebox.showwarning("提示", "您似乎没有存档")
def click_button_5_actions():
    utfliepath = a + "/Local/UNDERTALE"
    if os.path.exists(utfliepath):
        os.system("notepad"+" " + utfliepath + "/undertale.ini")
    else:
        messagebox.showwarning("提示", "您似乎没有存档")
window.mainloop()