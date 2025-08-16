score = [(90, 80), (85, 75), (90, 100)]
for i in score:
    print("%d번 학생의 총점은 %d점이고, 평균은 %.1f입니다." % (score.index(i) + 1, sum(i), sum(i) / 2))
