# school_alarm
school alarm. 

매시 정각과
매시 50분에
알람이 울립니다.

환경: windows11



## Check List
- [x] .exe
- [x] 볼륨 조절
- [ ] 시간 설정
- [ ] 오늘 날짜, 현재 시각
- [ ] 오늘 공부한 시간
- [ ] ...


<br/>

![스크린샷 2025-05-04 185232](https://github.com/user-attachments/assets/0c3790f2-0b68-4b4b-99f1-690172c296c6)


<br/>

### pyinstaller command option

```bash
pyinstaller --onefile -w --icon=bell.ico --add-data="school_bell.mp3;." alarm.py
```
