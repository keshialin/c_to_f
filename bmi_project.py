height = float(input('請輸入身高(公分):'))/100
weight = float(input('請輸入體重(公斤):'))
BMI = weight / height^2
if BMI < 18.5:
    print("過輕")
elif BMI >= 18.5 & BMI < 24:
    print("正常")
elif BMI >=24 & BMI < 30:
    print("輕度肥胖")
elif BMI >=27 & BMI < 35:
    print("中度肥胖")
else BMI >= 35:
    print("重度肥胖")