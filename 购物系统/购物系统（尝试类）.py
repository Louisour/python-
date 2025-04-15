import sys
users={}
current_user=None
def register():
    while True:

        user_name=input("请输入您的账户名：")
        if user_name in users:
            print("该用户名已被注册")
        else:
            password1=input("请输入您的密码：")
            password2=input("请确认您的密码：")
            if password1==password2:
                users[user_name]= {
                    "name":user_name,
                    "balance":0,
                    "password":password1
                }
                print(f"用户{user_name}注册成功！")
                break
            else:
                print("两次输入的密码不一致！")
def login():
    global current_user
    if not current_user:
        while True:
            user_name=input("请登录您的账号：")
            if user_name not in users:
                print("账号不存在！")
            else:
                user_password=input("请输入您的密码：")
                if user_password==users[user_name]["password"]:
                    print(f"用户{user_name}登录成功！")
                    current_user=user_name
                    break
                else:
                    print("密码错误！")
    else:
        print("已有账号登录！")

def logout():
    global current_user
    if current_user:
        print(f"{current_user}已登出！")
        current_user=None
    else:
        print("当前无账号登录。")
def deposit():
    global current_user
    if current_user:
        while True:

            amount=float(input("请输入您要充值的金额："))
            if amount>0:
                users[current_user]["balance"] += amount
                print(f"存入金额：{amount}，当前余额：{users[current_user]['balance']}")
                break
            else:
                print("充值金额不能小于零！")
    else:
        print("请先登录！")
def transfer():
    global current_user
    while True:
        if current_user:
            destination=input("请输入您要转账的用户：")
            if destination in users:
                amount=float(input("请输入要转账的金额："))
                if 0 < amount <= users[current_user]["balance"]:
                    users[current_user]["balance"] -= amount
                    print("转账成功！")
                    break
                else:
                    print("转账失败，请查询余额或者检查输入的金额是否正确。")
            else:
                print("用户不存在！")
def withdraw():
    global current_user
    while True:
        if current_user:
            amount=float(input("请输入您要提现的金额："))
            if 0 < amount <= users[current_user]["balance"]:
                users[current_user]["balance"] -= amount+amount*0.1
                print(f"提现成功！提现金额：{amount},余额：{users[current_user]['balance']}")
                break
            else:
                print("余额不足！")
def show_balance():
         print(f"余额：{users[current_user]['balance']}")

def main():
    while True:
        print("""
    0. 退出
    1. 注册功能
    2. 登录功能
    3. 充值功能
    4. 转账功能
    5. 提现功能
    6. 查看金额
    7. 查看流水???
    8. 购物功能???
    9. 查看购物车???
    10. 退出账号
    11. 管理员功能""")
        choice=input("请输入您的选择（1-11）：")
        if choice=="0":
            print("感谢您的使用！")
            sys.exit()
        elif choice=="1":
            register()
        elif choice=="2":
            login()
        elif choice=="3":
            deposit()
        elif choice=="4":
            transfer()
        elif choice=="5":
            withdraw()
        elif choice=="6":
            show_balance()
        elif choice=="10":
            logout()





if __name__ == '__main__':
    main()