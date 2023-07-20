# db 버전 표

| 버전                                          | product 내용                                   | review 내용                                                                            |
|---------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------|
| product, review                             | 떡볶이 60 품목에 대해서                               | 30페이지까지 리뷰 일괄 크롤링                                                                    |
| product_ver2, review_ver2                   | 떡볶이 top10, 광고 제외, 평균 평점 3 이상                 | 텍스트 전처리, 도움이 되었어요 1 이상, 글자수 50~500                                                   |
| product_ver3, review_ver3                   | 치킨 top10, 광고 제외, 평균 평점 3 이상                  | 텍스트 전처리, 도움이 되었어요 1 이상, 글자수 50~500                                                   |
| product_ver4, review_ver4                   | [떡볶이, 치킨 한 테이블에 모음] top10, 광고 제외, 평균 평점 3 이상 | 텍스트 전처리, 도움이 되었어요 1 이상, 글자수 50~500                                                   |
| product_ver5, review_ver5                   | 품목 30개, top10, 광고 제외, 평균 평점 3 이상             | 텍스트 전처리, 도움이 되었어요 1 이상, 글자수 50~500                                                   |
| product_ver6, review_ver6                   | 품목 10개, top10, 광고 제외, 평균 평점 3 이상             | 텍스트 전처리, 도움이 되었어요 1 이상, 글자수 50~500, 맞춤법 검사, \s -> ' ' 처리                             |
| review_ver2_1, review_ver3_1, review_ver4_1 | 떡볶이 top10, 광고 제외, 평균 평점 3 이상                 | 텍스트 전처리, 도움이 되었어요 1 이상, 글자수 50~500                       맞춤법 검사, \s -> ' ' 처리, 온점 보존 |
| TODO: product7, review7                     |||
