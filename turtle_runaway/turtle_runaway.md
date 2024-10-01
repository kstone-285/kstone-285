## 🐢 도망쳐 거북아! 🐢

**해당 게임은 추격자로부터 최대한 오랫동안 도망치는 게임입니다.**

좌측 상단의 **타이머**가 당신의 점수가 됩니다.  
`time` 라이브러리를 사용하여 **시간 측정**을 매우 짧은 간격(50ms)으로 하게 됩니다.

---

- 약 **30픽셀**의 반지름이 당신의 히트박스입니다.  
- 닿는 순간 **패배**하게 됩니다.

추격자 거북이는 해당 코드를 바탕으로 당신의 **위치**와 **각도**를 실시간으로 계산하여 계속해서 쫓아올 것입니다.

dx = opp_pos[0] - runner_pos[0] 당신과 추격자의 **상대적 좌표차이** 입니다.  
dy = opp_pos[1] - runner_pos[1]  
       
angle_to_opponent = math.degrees(math.atan2(dy, dx)) 머리를 돌릴 **각도**를 설정합니다.  
heading_diff = angle_to_opponent - self.heading()  

---

**당신이 지칠지, 거북이가 지칠지 시험해보는 것은 어떨까요?**

if(is_catched) :  
    self.paused = True  
    self.display_score()  
    return  

**추격자는 당신이 잡힐 때 까지 멈추지 않을 것입니다..**