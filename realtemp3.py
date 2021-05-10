from typing import Any, Union

import pandas as pd
import streamlit as st
from playsound import *

st.title('체감온도에 따른 건강관리 및 코디 제안')
st.markdown("___")

st.markdown('### **체감 온도**란?')
st.write(" 체감 온도(體感溫度, 영어: Apparent temperature, Feels like temperature)는 바람에 의해 피부에 느껴지는 온도이다. 체감온도는 주로 실제 온도보다 낮은데, 이는 체온이 실제 온도보다 높기 때문이다. 우리는 추울 때나 더울 때나 몹시 불쾌한 느낌을 갖게 된다. 이는 몸으로부터 외부에 필요 이상의 열을 빼앗기고 있거나, 또는 몸체로부터 외부에 적당량의 열을 발산하지 못하게 되든지, 반대로 열이 몸에 스며들고 있기 때문인 것이다. 쾌적한 기상조건인지 아닌지는 이와 같이 신체를 통하여 열의 출입, 즉 기상환경과의 열교환과 관계가 있는 것이다.")
st.latex(r'\textcolor{red}{체감온도}(\degree C) = 13.12 + 0.6215 \times T-11.37 \times V^{0.16} + 0.3965 \times T \times V^{0.16}')
st.latex(r'기온=T(\degree C),　풍속=V(m/s)')
st.markdown("___")

number1 = st.number_input('기온 측정값')
st.write('#### 현재 기온 측정값=', number1)

number2 = st.number_input('풍속 측정값')
st.write('#### 현재 풍속 측정값=', number2)

df = pd.read_csv('./tem.xls')
#df = pd.read_csv('C:\\Users\\sec\\PycharmProjects\\codeitPython\\REALTEMP\\tem.csv')
dataset = df.values

X = dataset[:, 0:2]
Y = dataset[:, 2]
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(X,Y,random_state=42)

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)

test_poly = poly.transform(test_input)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train_poly, train_target)
sample = PolynomialFeatures(include_bias=False)
sample.fit([[number1, number2]])
sample_poly = sample.transform([[number1, number2]])
result = lr.predict(sample_poly)

print(result)
st.markdown("## 현재 **체감온도**는"+ str(result) +"입니다.")
if result<3:
    st.markdown("___")
    st.write("# <건강관리 **TIP**>")
    st.markdown("### 너무 너무 추워요. 체온 유지를 위해 두꺼운 옷을 입어야 해요. 면역이 떨어지지 않게 따뜻한 물을 자주 마셔 주세요.")
    st.image("https://cdn.gjdream.com/news/photo/old/news/contents/UPFILE/2007/2007110545854.jpg", caption=('면역을 올려 감기를 극복합시다!'), width=500)
    st.markdown("___")

    st.title('**<코디 제안>**')

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.subheader("최대한 감싸는 코디")
        st.image("http://www.econovill.com/news/photo/202001/382219_296048_137.JPG" , caption=('추위에 장사없어요! 최대한 몸을 감싸고 따뜻하게 하는 게 최고겠지요~'), width=200 )

    with col2:
        st.subheader("롱패딩 코디")
        st.image("https://mblogthumb-phinf.pstatic.net/MjAxOTEyMDdfMTE1/MDAxNTc1NzI2NDYxNDc5.X8B_3KdBnESnXTgA6Ka0YDUzkJ8UAAuqxQvLkB45NlYg.0r5O_nSsPS2SpMBzKKnEYPdVn8PrQDBuWRz-WoGZTL0g.JPEG.leahhhon/1575726466100.jpg?type=w800" , caption=('첫 눈도 내리고 얼굴도 시리고 손발이 꽁꽁 시릴 정도로 추워진 겨울 날씨엔 역시나 롱패딩이 최고죠~'), width=200)
    with col3:
        st.subheader("롱코트 코디")
        st.image("https://i.pinimg.com/564x/02/ec/77/02ec779a42603bb2cd3a39b1937a1707.jpg", caption=('롱코트 영하날씨 코디 날씨가 추워도 롱코트 포기할 수 없지욤 추운날에도 따숩고 예쁘게 입어봐요~'), width=200 )

    st.warning('**두꺼운 옷으로 코디해주세요. 추워 보이면 없어 보여요**')
    playsound('tell1.mp3')

elif result<18:
    st.markdown("___")
    st.write("# <건강관리 **TIP**>")
    st.markdown("### 날씨가 쌀쌀하네요. 일교차가 심할 수 있으니 감기 조심하시고 외투를 준비하시는 것을 추천합니다.")
    st.image("http://4.bp.blogspot.com/-dMD1GcHNIEQ/Um-Vx4qVJ0I/AAAAAAAAAbo/QnG8zGJk2PM/s640/2010-09-06_19%253B50%253B32.jpg", caption=('면역을 올려 감기를 극복합시다!'), width=500)
    st.markdown("___")

    st.title('**<코디 제안>**')

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.subheader("가벼운 자켓 코디")
        st.image("data:image/jpeg;base64,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" , caption=('간절기 코디'), width=200 )

    with col2:
        st.subheader("댄디룩 코디")
        st.image("data:image/jpeg;base64,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" , caption=('맥코트와 코튼 팬츠를 매치한 댄디룩으로 멋스러움을 연출하세요~'), width=200)
    with col3:
        st.subheader("긴아우터와 코디")
        st.image("http://img.ezday.co.kr/cache/board/2010/05/02/7be0fb5a59db81a5fcedfa7ab94f0ea4.jpg", caption=('라이더 자켓이 비교적 짧은 기장의 자켓이였다면, 긴 아우터와 매치하는 방법도 있답니다. 정장풍의 검정색 자켓이나얇은 검정색 긴 가디건과 연출해도 좋아요.'), width=250 )
    st.warning('**다양한 아이템으로 멋스럽게 연출해 보세요!**')
    playsound('tell2.mp3')

elif result<26:
    st.markdown("___")
    st.write("# <건강관리 **TIP**>")
    st.markdown("### 날씨가 정말 좋군요. 이렇게 따뜻한 날씨에는 야외활동을 적극 추천합니다. 야외 활동 후에는 개인 위생 관리에 신경써 주세요~")
    st.image("https://cdn.dkilbo.com/news/photo/202008/308450_206404_0146.jpg", caption=('위생 관리 철저히 하기!'), width=500)
    st.markdown("___")

    st.title('**<코디 제안>**')

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.subheader("가벼운 캐주얼 룩")
        st.image("http://image.musinsa.com/images/codimap/list/2021050411433600000077404.jpg" , caption=('스트라이프 패턴의 티셔츠와 편안한 핏의 조거 팬츠로 연출한 캐주얼 룩이 정말 산듯하네요~'), width=200 )

    with col2:
        st.subheader("네츄럴 코디")
        st.image("https://scontent.cdnsnapwidget.com/vp/9e4cd9e8d8809790479a968bd453fb52/5B7E7BB9/t51.2885-15/e35/31556919_970091903156775_7889007298071232512_n.jpg" , caption=('가벼운 소재감! 깔끔한 디자인의 낙낙한 핏감! 네츄럴하게 데일리한 코디를 연출해 보세요~'), width=200)
    with col3:
        st.subheader("데엘리룩 코디")
        st.image("https://contents.lotteon.com/itemimage/LO/12/55/81/62/94/_1/25/58/16/29/5/LO1255816294_1255816295_1.jpg/dims/resizef/720X720", caption=('원피스 입기편한 가벼운 러블리한 여성 코디 데일리룩! 어때요?'), width=250 )
    st.warning('**캐쥬얼하고 산듯하게 따뜻한 날씨를 표현해 보세요~**')
    playsound('tell3.mp3')


else:
    st.markdown("___")
    st.write("# <건강관리 **TIP**>")
    st.markdown("### 너무 너무 더워요. 이렇게 더운 날씨에는 외부활동을 가급적 삼가하고 탈수의 위험이 있으니 물을 자주 섭취해 주세요~ 실내 에어컨 환경에 너무 오래 노출되는 것은 오히려 건강에 좋지 않아요~")
    st.image("data:image/jpeg;base64,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", caption=('무더위 이렇게 극복합시다!'), width=500)
    st.markdown("___")

    st.title('**<코디 제안>**')

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.subheader("여름 유행 남성 팬츠 스타일")
        st.image("https://t1.daumcdn.net/cfile/blog/1528A63F4E38C63E2E" , caption=('계절마다 유행하는 패션 스타일이 있는데요 특히나 올해에는 남성 팬츠의 길이가 점점 짧아지는 추세인듯 해요~'), width=200 )

    with col2:
        st.subheader("청바지 코디")
        st.image("https://blog.kakaocdn.net/dn/96WZi/btqESpBgJY6/y13MSokrPVc058Vg2beHe1/img.jpg" , caption=('여름에도 가장 쉽게 코디할 수 있는 청바지 코디! 계절에 상관없이 코디할 수 있는 제일 베이직한 아이템이죠~'), width=200)
    with col3:
        st.subheader("스트릿패션 코디")
        st.image("https://i.pinimg.com/474x/39/95/3d/39953dd4e4e47c292bc465259bb04af5.jpg", caption=('스트릿패션 코디로 시원함과 자연스러움을 모두 표현해 보세요~'), width=200 )
    st.warning('**무더위를 시원한 옷차림으로 날려 버리자!**')
    playsound('tell4.mp3')

