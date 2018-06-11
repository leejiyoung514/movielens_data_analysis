import numpy as np

data=np.loadtxt("d:/data/movielens/ratings.dat",\
                delimiter="::", dtype=np.int64) #백만까지가서
#데이터의 첫 5행만 확인
print(data[:5,:])

#데이터의 형태 확인
print(data.shape)

#전체 평균 평점 계산
#행범위:열범위
mean_rating_total=data[:,2].mean()
print(mean_rating_total)

#사용자 아이디 수집
user_ids=np.unique(data[:,0])
print(user_ids)

#사용자별 평균값 저장할 배열
mean_values=[]
for user_id in user_ids:
    #첫번째 열 아이디
    #현재 user_id가 1이라면 user_id가 1인 행들만 추줄해서
    #data_for_user에 저장
    #data 중에서 모든행, 0번필드가 user_id인 행의 모든 컬럼
    data_for_user=data[data[:,0]==user_id,:]
    #2번째 인덱스(평점)에 해당하는 값의 평균값
    value=data_for_user[:,2].mean()
    #사용자아이다와 평균값을 배열에 추가
    #리스트 안에 리스트가 들어가므로 2차원 리스트로 만들어짐
    mean_values.append([user_id,value])

#사용자 아이디별 평점 확인
print(mean_values[:5])
#리스트를 넘파이 배열로 변환
mean_array=np.array(mean_values, dtype=np.float32)
print(mean_array[:5])
print(mean_array.shape)

#계산 결과를 csv파일로 저장
np.savetxt("d:/data/movielens/result.csv",
           mean_array, fmt="%.1f", delimiter=",")
#파일이 만들어졌는지 확인
