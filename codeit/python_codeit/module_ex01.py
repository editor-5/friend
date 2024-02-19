import pandas as pd

# 사전에서 DataFrame 생성
data = {'이름': ['영희', '철수', '미영', '동민'],
        '나이': [25, 30, 35, 40],
        '도시': ['서울', '부산', '대전', '광주']}

df = pd.DataFrame(data)

# DataFrame 표시
print(df)
