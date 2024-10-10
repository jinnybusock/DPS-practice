# numpy와 matplotlib.pyplot 라이브러리 불러오기
#numpy: 배열 계산, matplotlib: 그래프 그리기

import numpy as np
import matplotlib.pyplot as plt

# 시퀀스의 시작 값과 끝 값 정의
start= 0
end= 20
# 임펄스 위치 정의
impulse= 3

# np.arange() 함수로 discrete-time 시퀀스 생성
# start에서 end까지의 값을 가지는 배열 생성
dt_seq= np.arange(start, end+1)

# 위에서 정의한 discrete-time 시퀀스 출력
print(f"Start: {start}, End: {end}, Impulse: {impulse}")
print("Sequence length: ", end-start)
print("Discrete-time sequence: ", format(dt_seq))

# 임펄스 시퀀스 생성
# (i+ start) 값이 impulse 값인 3과 같을 때만 1 을 할당하고, 그 외는 0을 할당하기
unit_sample_list= [1 if (i+start) == impulse else 0 for i in range(end+1)]
# 리스트를 numpy 배열로 변환
unit_sample_array= np.array(unit_sample_list)

print(f"Unit sample sequence: {unit_sample_array}")