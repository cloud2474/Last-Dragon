from colorama import Fore,Style
from sys import exit
import random


#cmd trace
#python -m trace --trace -C . D:\py\123\LastDragon\LastDragon.py

#pyinstaller --onefile --distpath D:\py\123\output\dist --workpath D:\py\123\output\build --specpath D:\py\123\output "D:\py\123\LastDragon\LastDragon.py"

#彩色文字
def print_colored(text,color,style=Style.NORMAL):
    print(color + style + text + Style.RESET_ALL)

#加粗文字
def print_stress(text):
    print(Style.BRIGHT + text + Style.RESET_ALL)

#调试数据
def print_debug(text,variable=None):
    if sys.mode == 0:
        if variable is not None:
            print(text,variable)
        else:
            print(text)

#input异常处理
#示例  choice = input_('你选择..?\n',[1,4]) 有效输入范围为1~4
def input_(text,input_range): 
    while True:
        try:  #尝试将输入转化为int
            user_input = int(input(text))
        except: #如果输入无法转化为int
            print('无效输入') 
            continue #continue循环,要求重新输入
        valid_range = [] #创建有效输入list
        for i in range(input_range[0],input_range[1]+1): #遍历有效输入的范围(input_range为list，进行索引获取传入range的起始值和结束值，结束值+1使得range生成的结束值等同于input_range结束值)
            valid_range.append(i) #将有效输入存储进list
        if user_input in valid_range: #判断用户输入是否在有效输入列表中
            return user_input #返回用户输入,结束函数
        else: #当用户输入不在有效输入列表中
            print('无效输入')
            continue #continue循环,要求重新输入

#创建类sys储存系统变量
class sys:
    def __init__(sys):
        sys.time = 5
        sys.day = True
        sys.Day = 1
        sys.night = False
        sys.step = 0
        sys.round = 0
        sys.mode = 1
        sys.Ending = False
        # mode0为调试模式, mode1为正常游玩
    
    def Ending1(self):
        input('你杀死了恶龙,从此和公主过上了幸福的生活')
        print_stress('Happy End')
        sys.Ending = True
        Game()
    
    def Ending2(self):
        print_stress('Game Over..')
        sys.Ending = True
        Game()

    def Ending3(self):
        input('你从此和旅行者过上了幸福的生活')
        input('至于公主?希望她幸福')
        print_stress('Happy End?')
        sys.Ending = True
        Game()

    def Ending4(self):
        input('拯救公主什么的,怎么可能做得到啊')
        input('你自言自语着,看着远方的山脉一点点消失在视线之中')
        input('回家..')
        print_stress('Normal End')
        sys.Ending = True
        Game()

    def Ending5(self):
        input('在成为沼泽的一部分之前,你能做只是最后一次仰望天空')
        print_stress('Bad End')
        sys.Ending = True
        Game()

    def Ending6(self):
        input('你成为了一个饿死鬼')
        print_stress('Bad End')
        sys.Ending = True
        Game()

    def Ending7(self):
        input('你失去了意识')
        input('当你再次醒来时,已经有了一个新的身份')
        input('奴隶')
        print_stress('Bad End')
        sys.Ending = True
        Game()

    def Ending8(self):
        input('你失去了意识')
        input('不知过了多久,你在恍惚中睁开了眼睛')
        input('你想试着站起身来,但失败了')
        input('你被随意的丢到木屋的角落,你的脖子上紧紧缠绕着一根麻绳,绳子的另一头系在了旁边的大锅上')
        input('锅里煮着的是你曾经的肢体')
        print_stress('Bad End')
        sys.Ending = True
        Game()

    def Ending9(self):
        input('你成为了Dragon的???')
        input('你和恶龙和公主幸福的生活在了一起')
        print_stress('Happy End?')
        sys.Ending = True
        Game()
sys = sys()


#主程序
def Game():
    if sys.Ending:
        input('')
        exit()

    You.hungry(1.5)
    You.hitpoint_state()
    You.status_check()
    sys.round += 1
    sys.time += 1

    print_debug('step:',sys.step)
    print_debug('hunger:',You.hunger) 
    print_debug('time:',sys.time)

    if You.drunkenness >= 5: 
        You.drunkenness -= 5

    if sys.time >= 24:
        #print_stress('抬头,有星光')
        sys.time -= 24
        sys.Day += 1

    print(f'Day{sys.Day}')

    if 6 <= sys.time < 18:
        if sys.time == 6:
            print_colored('太阳..再一次',Fore.YELLOW,Style.BRIGHT)
        sys.day = True
        sys.night = False
        print_colored('白日',Fore.YELLOW,Style.BRIGHT)
    elif 18 <= sys.time < 24 or sys.time < 6 :
        if sys.time == 18:
            print_colored( '太阳落山了..',Fore.BLACK,Style.BRIGHT)
        print_colored('夜幕',Fore.BLACK,Style.BRIGHT)
        sys.day = False
        sys.night = True
    
    if 0 <= sys.step < 20:
        town.action()
    elif 20 <= sys.step <40:
        plains.action()
    elif 40 <= sys.step <60:  #当step>40
        if Golem.alive:       #如果上一区域的BOSS仍然存活
            fight(Golem)      #进入战斗
            sys.step = 39     #重置step为地图交界时的数值
            Game()
        else:
            swamp.action()
    elif 60 <= sys.step <80:
        if Death_Knight.alive:
            fight(Death_Knight)
            sys.step = 59
            Game()
        else:
            forest.action()
    elif sys.step >= 80:
        if The_Big_Bad_Wolf.alive:
            fight(The_Big_Bad_Wolf)
            sys.step = 79
            Game()
        else:
            mountain.action()

    if You.deep < 10:
        pass
    elif You.deep < 15:
        print_stress('你感觉自己的双脚逐渐陷入了泥中..')
        You.status('slow',10,1)
    elif You.deep < 20:
        print_stress('泥潭没过了你的膝盖..')
        You.status('slow',30,1)
    elif You.deep < 30:
        print_stress('你一半的身体几乎都陷入了黑泥之中..')
        You.status('slow',50,1)
    elif You.deep <40:
        sys.Ending5()


#战斗模块
def fight(entity):
    You.in_fight = True
    #hasattr()函数用于判断对象是否具有指定的属性或方法。返回一个布尔值。(常用的还有setattr,getattr)
    if hasattr(entity,'intro'): #如果敌人存在intro方法
        print('')
        entity.intro()
    while You.hitpoint > 0 and entity.hitpoint > 0 : #当你和敌人的Hp都大于0,重复战斗流程
        You.status_check()
        You.hitpoint_state()
        sys.round += 1
        print_debug('round:',sys.round)
        print_debug('HP:',You.hitpoint)
        print('EnemyHP:',entity.hitpoint)
        You.Flag_dodge = False #重置上回合你的选择
        You.Flag_escape = False 

        print('\n1.攻击\n2.闪避\n3.打开背包\n4.逃跑')
        choice = input_('你选择..?\n',[1,4])
        print('')
        if choice == 1:
            You.attack(You.attack_damage,entity)
        elif choice == 2:
            You.dodge()
        elif choice == 3:
            print('你打开了背包')
            You.open_backpack()
        elif choice == 4:
            You.escape()

        if You.Flag_escape == True:
            print('你逃跑了')
            print('你还不想死在这里,起码现在不想')
            break

        if entity == Mud:
            Traveler.attack(Mud)

        if entity.hitpoint >0: #如果敌人的生命值大于0
            entity.attack(You) #敌人进行攻击
        
        input('')

    if You.hitpoint > 0: #如果战斗结束后你还活着
        if hasattr(entity,'default_hitpoint'):
            entity.hitpoint = entity.default_hitpoint #重置敌人生命值
        You.in_fight = False


#Character And Monster
class You:
    def __init__(self):
        self.max_hitpoint = 30 #生命上限
        self.hitpoint = 30 #生命值
        self.attack_damage = 5 #攻击力
        self.agile = 30  #敏捷值,等同于自身的闪避率
        self.accuracy = 70 #命中率,应用于具有闪避方法的敌人
        self.gold = 30 #银币
        self.hunger = 66.5 #饥饿值
        self.drunkenness = 0 #醉酒值
        self.deep = 0 #深度
        self.backpack = [Bread,Apple] #背包,储存物品信息
        self.backpack_space = 30 #背包空间
        self.status_dict = {} #储存状态信息
        self.in_fight = False #是否在战斗中
        self.Angel = False
        self.get_angel = False


    def open_backpack(self):
        if not self.backpack and self.gold == 0:  #当你的背包为空列表 and 你没有任何银币 (空的数据容器返回布尔值False)
            input('背包中什么都没有')
        elif not self.backpack: #当你的背包为空列表,但是你的银币不等于0
            input(f'背包中只有{self.gold}枚银币')
        else: #当你的背包不为空列表
            print(f'你有{self.gold}枚银币')
            print('0.关上背包')
            number = 0 #初始化number(序号)
            for item in self.backpack: #遍历背包
                number += 1   #每遍历一个物品,序号加1
                print(f'{number}.{item.name}')  #打印序号和对应的物品名称
            choice = input_('你选择..?\n',[0,number])  #输入查看的物品序号,赋值给choice
            if choice == 0: #当选择是关闭背包
                return
            else: #当选择不是关闭背包
                choice -= 1  #背包列表的index从0开始,显示从1开始，所以需要-1
                self.backpack[choice].intro() #获取背包中的第choice个元素,执行其intro方法(self.backpack[choice]返回背包中的第choice个元素)
                if hasattr(self.backpack[choice],'use'): #如果物品存在'use'方法
                    print('1.使用\n2.放回背包\n3.丢弃')  #选择是否使用物品
                    action_choice = input_('你选择..?\n',[1,3])
                    if action_choice == 1: 
                        self.backpack[choice].use() #执行其use方法
                        if self.in_fight: #如果你正在战斗,使用一个物品后关闭背包
                            return
                    elif action_choice == 2:
                        input(f'你将{self.backpack[choice].name}放回了背包')
                    elif action_choice == 3:
                        input(f'你丢弃了{self.backpack[choice].name}')
                        self.backpack.remove(self.backpack[choice])
                elif isinstance(self.backpack[choice],Food): #isinstance判断物品是否为类Food的实例
                    print('1.吃\n2.不吃\n3.丢弃')
                    action_choice = input_('你选择..?\n',[1,3])
                    if action_choice == 1: 
                        self.backpack[choice].eat()
                        if self.in_fight: #如果你正在战斗,使用一个物品后关闭背包
                            return
                    elif action_choice == 2:
                        input(f'你将{self.backpack[choice].name}放回了背包')
                    elif action_choice == 3:
                        input(f'你丢弃了{self.backpack[choice].name}')
                        self.backpack.remove(self.backpack[choice])
                else:
                    print('1.放回背包\n2.丢弃')
                    action_choice = input_('你选择..?\n',[1,2])
                    if action_choice == 1:
                        input(f'你将{self.backpack[choice].name}放回了背包')
                    elif action_choice == 2:
                        if hasattr(self.backpack[choice],'effect'): #如果物品存在被动效果
                            self.backpack[choice].del_effect() #删除被动效果
                        input(f'你丢弃了{self.backpack[choice].name}')
                        self.backpack.remove(self.backpack[choice])
                self.open_backpack() #返回背包界面
            
    def obtain(self,item):
        print()
        # print(f'你捡起了{item.name}') #//
        self.backpack.append(item)  #将物品先加入背包以便于计算总空间  (self.backpack和You.backpack在此处都可以正常运行.但self.是实例变量,You.是类变量.类变量所有实例共享,实例变量每一个实例单独计算)
        total = sum(item.space for item in self.backpack) #计算当前背包内物品总空间(生成器表达式,以item遍历self.backpack,生成item.space,再用sum求和)
        # print(f'背包剩余空间{self.backpack_space - total +item.space}') #//
        # print(f'物品所需空间{item.space}')#//
        if total > self.backpack_space: #如果物品占用空间大于背包空间
            print(f'背包已满,无法获得{item.name}') 
            self.backpack.remove(item) #移除本次获得的物品
            print(f'1.打开背包\n2.丢弃{item.name}')
            choice = input_('你选择..?\n',[1,2])
            if choice == 1:
                self.open_backpack()
                self.obtain(item) #再次获得该物品,重新执行该方法判断背包空间是否足够(递归,调用自身)
                return #return结束本次函数!防止递归时多次执行后续代码(递归时当前层的后续代码会在递归返回到该层时继续执行,而不是被放弃)
            elif choice == 2:
                print(f'你丢弃了{item.name}')
        else: #当背包空间足够时
            print(f'你获得了{item.name}')  
            if hasattr(item,'effect'): #如果物品存在'effect'方法(被动效果)
                item.effect() #触发被动效果
        #此处以下的代码(直接处于def下执行的)会因为前面的递归而被执行多次!!(已解决)
        #不在后面再写代码就可以正常运行,一定要写的话就将上方递归改为while(现在可以加了)
        #凌晨三点在床上想到在递归时加一个return就可以解决问题了:)
        #(递归调用后的代码在每一层都被保留并等待执行，直到递归返回)
        

    def lose_hitpoint(self,hurt,attacker=None):
        self.hitpoint -= hurt
        print_debug(f'你受到了{hurt}点伤害') #测试，实际游玩中不显示伤害
        if self.hitpoint <= 0:
            if You.Angel: 
                self.hitpoint = 1
            else:
                if attacker is Stranger:
                    sys.Ending7()
                elif attacker is Witch:
                    sys.Ending8()
                else:
                    sys.Ending2()

    def hitpoint_state(self):
        if self.hitpoint <=6:
            print_colored('你的意识逐渐模糊..世界似乎在缓缓远离你',Fore.RED,Style.DIM)
        elif self.hitpoint <=14:
            print_colored('鲜血从伤口涌出,你的体力随之流逝..',Fore.RED)
        elif self.hitpoint <=21:
            print_colored('你受了一些轻伤',Fore.RED,Style.DIM)
        
    def heal(self,value):
        self.hitpoint += value
        if self.hitpoint > self.max_hitpoint: #如果治疗后的HP大于上限
            self.hitpoint = self.max_hitpoint #则将HP等同于上限
    
    def attack(self,damage,entity):
        print('你挥剑向前砍去')
        damage += random.randint(-2,2) #伤害随机,范围为攻击力的+-2
        if hasattr(entity,'dodge'): #判断目标是否具有闪避方法
            entity.dodge(damage)
        else:
            print(f'你造成了{damage}点伤害')
            entity.lose_hitpoint(damage)

    def counter_attack(self,entity):
        print('你抓住机会,挥剑反击')
        damage = self.attack_damage + random.randint(-2,2)
        print(f'你造成了{damage}点伤害')
        entity.lose_hitpoint(damage)

    def status(self,status,value,round): #status:状态类型;value:修正值;round:持续回合
        if status == 'strength': #如果传入的状态为'力量'
            if 'strength_value' in self.status_dict: #检查是否已经具有一种力量效果
                self.attack_damage -= self.status_dict['strength_value'] #如果有,取消之前的力量修正
            self.status_dict['strength_value'] = value #将值写入status_dict中储存('strength_value'作为键,value作为值)
            self.status_dict['strength_end_round'] = sys.round + round #计算状态结束的回合(等于当前回合+持续回合),写入status_dict储存('strength_end_round'作为键,结束回合作为值)
            self.attack_damage += value #攻击力增加等同于value的数值
            print_debug(f'获得力量效果,攻击力上升{self.status_dict['strength_value']}')#调试
            print_debug(f'效果将在第{self.status_dict['strength_end_round']}回合结束')#调试

        if status == 'weak':
            if 'weak_value' in self.status_dict:
                self.attack_damage += self.status_dict['weak_value']
            self.status_dict['weak_value'] = value
            self.status_dict['weak_end_round'] = sys.round + round
            self.attack_damage -= value
            
        if status == 'agile':
            if 'agile_value' in self.status_dict:
                self.agile -= self.status_dict['agile_value']
            self.status_dict['agile_value'] = value
            self.status_dict['agile_end_round'] = sys.round + round
            self.agile += value

        if status == 'slow':
            if 'slow_value' in self.status_dict:
                self.agile += self.status_dict['slow_value']
            self.status_dict['slow_value'] = value
            self.status_dict['slow_end_round'] = sys.round + round
            self.agile -= value

        if status == 'poison':
            self.status_dict['poison_value'] = value
            self.status_dict['poison_end_round'] = sys.round + round

        if status == 'drunk':
            if 'drunk_value' in self.status_dict:
                self.accuracy += self.status_dict['drunk_value']
                self.agile += self.status_dict['drunk_value']
            self.status_dict['drunk_value'] = value
            self.status_dict['drunk_end_round'] = sys.round + round
            self.accuracy -= value
            self.agile -= value

        if status == 'angel':
            You.Angel = True
            self.status_dict['Angel_end_round'] = sys.round + round
        
        print_debug(self.status_dict) #调试
    
    def status_check(self):
        if 'strength_value' in self.status_dict: #如果当前存在力量效果
            if self.status_dict['strength_end_round'] == sys.round: #如果效果结束回合等于当前回合
                self.attack_damage -= self.status_dict['strength_value'] #取消力量修正
                print_debug(f'移除力量效果,攻击力降低{self.status_dict['strength_value']}')#调试
                del self.status_dict['strength_value'] #从字典中删除状态信息
                del self.status_dict['strength_end_round']
            else:
                print_stress('你感到了力量')

        if 'weak_value' in self.status_dict:
            if self.status_dict['weak_end_round'] == sys.round:
                self.attack_damage += self.status_dict['weak_value']
                print_debug(f'移除虚弱效果,攻击力上升{self.status_dict['weak_value']}')
                del self.status_dict['weak_value']
                del self.status_dict['weak_end_round']
            else:
                print_stress('你感到虚弱')

        if 'agile_value' in self.status_dict:
            if self.status_dict['agile_end_round'] == sys.round:
                self.agile -= self.status_dict['agile_value']
                print_debug(f'移除agile效果,agile降低{self.status_dict['agile_value']}')
                del self.status_dict['agile_value']
                del self.status_dict['agile_end_round']
            else:
                print_stress('你感到轻盈')

        if 'slow_value' in self.status_dict:
            if self.status_dict['slow_end_round'] == sys.round:
                self.agile += self.status_dict['slow_value']
                print_debug(f'移除slow效果,agile上升{self.status_dict['slow_value']}')
                del self.status_dict['slow_value']
                del self.status_dict['slow_end_round']
            else:
                print_stress('你感到迟缓')
        
        if 'poison_value' in self.status_dict:
            if self.status_dict['poison_end_round'] == sys.round or Antidote.used:
                print_debug('移除中毒效果')
                del self.status_dict['poison_value']
                del self.status_dict['poison_end_round']
            else:
                print('你觉得自己好像中毒了')
                self.hitpoint -= self.status_dict['poison_value']
                print_debug(f'你受到了{self.status_dict['poison_value']}点中毒伤害')     

        if 'drunk_value' in self.status_dict:
            if self.status_dict['drunk_end_round'] == sys.round:
                self.accuracy += self.status_dict['drunk_value']
                self.agile += self.status_dict['drunk_value']
                print_debug(f'移除drunk效果,accuracy,agile上升{self.status_dict['drunk_value']}')
                del self.status_dict['drunk_value']
                del self.status_dict['drunk_end_round']
        
        if You.Angel:
            if self.status_dict['Angel_end_round'] == sys.round:
                self.heal(self.max_hitpoint//2)

        print_debug(self.status_dict) #调试
        
    def dodge(self):
        self.Flag_dodge = True #说明玩家选择了闪避

    def escape(self):
        input('你尝试逃跑')
        if random.randint(1,6) <= 2:
            input('成功了')
            self.Flag_escape = True
        else:
            input('失败了')
            self.Flag_escape = False
            
    def surrender(self):
        # sys.Ending4 = True
        # Game()
        pass
    
    def hungry(self,value,rest=False):
        self.hunger -= value
        if rest == True: #(如果是休息/睡觉导致的饥饿，不输出状态信息，因为Game中会输出一次)
            return
        if self.hunger <= 0:
            sys.Ending6()
        elif self.hunger <= 25:
            print('你很饿')
            You.status('weak',4,1)
        elif self.hunger <= 40:
            print('你饿了')
            You.status('weak',2,1)  
        elif self.hunger >= 80:
            print('你吃的非常饱')
            You.status('slow',15,1)

    def eat(self,value):
        input('吃吃吃.')
        input('吃吃..')
        input('吃...')
        self.hunger += value
        if self.hunger > 100:
            self.hunger = 100    
    
    def drink(self,value):
        input('喝酒..')
        input('喝..')
        self.drunkenness += value
        if self.drunkenness >= 60:
            self.status('drunk',50,15)
        elif self.drunkenness >= 40:
            self.status('drunk',30,10)
        elif self.drunkenness >= 20:
            self.status('drunk',10,5)
            print_stress('你感到自己有些醉了..')

    def pay(self,value):  #这个方法没有任何的实际意义,但是它可以让代码看起来好看一些
        if self.gold < value:  #好的我发现它的意义了,就是让你不能没钱了还白吃白喝
            print('你没有足够的银币')
            return False
        self.gold -= value
        return True

    def rest(self):
        self.heal(1)
        input('\n你休息了一会..')
        print('你感觉好一些了')
        print('1.启程\n2.再休息一会\n3.睡觉')
        choice = input_('你选择..?\n',[1,3])
        if choice == 1:
            Game()
        elif choice == 2:
            sys.time += 1
            self.hungry(1.5,rest=True)
            self.rest()
        elif choice == 3:
            self.sleep()

    def sleep(self):
        print('好梦..')
        self.heal(10)
        input('...')
        input('..')
        input('.')
        dream = random.choices(['你梦见了什么吗..?',
                                '你梦见自己被怪物撕咬破碎..',
                                '在梦中,你和公主幸福的生活在一起..',
                                '你梦见了海边的落日,红色与金色交融在一起..'],weights=[55,30,10,5])[0]
        input(dream)
        sys.time += 7
        self.hungry(10.5,rest=True)
        print('欢迎回来')
        Game()
class Dragon:
    def __init__(self):
        self.hitpoint = 50

    def intro(self):
        print('龙睁开了眼眸..')

    def attack(self,entity): #从不同的攻击方式中按照权重选择一个
        attack = random.choices([self.attack1,self.attack2],weights=[70,30])[0] #(choices方法返回list，使用[0]选取第一个元素)
        attack(entity)  #执行被选中的攻击方法
         
    def attack1(self,entity):
        damage =random.randint(6,9)
        print('龙挥出致命的爪击')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:     #当玩家选择闪避
                print('你避开了龙的利爪')        #当(1,100)随机数小于敏捷值，闪避成功
                damage = 0                     #将本次攻击的伤害设置为0
                You.counter_attack(Dragon)     #进行反击
            else:     #当(1,100)随机数不小于30，闪避失败
                print('你没有想象中的那么敏捷') 
        if damage > 0:                       #如果本次攻击的伤害最终大于0，结算伤害
            print('龙的利爪上淌着你的鲜血')
            entity.lose_hitpoint(damage)

    def attack2(self,entity):
        damage =random.randint(10,12)
        print('龙喷出骄傲的火焰')
        if You.Flag_dodge == True: 
            if random.randint(1,100) <= You.agile:  
                print('你躲过了一部分火焰')
                damage = 1
                You.counter_attack(Dragon)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('火焰灼烧着你的身体')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
        
    def dead(self):
        print_colored('龙的鲜血模糊了你的视野',Fore.RED,Style.BRIGHT)
        sys.Ending1()
class Traveler:
    def __init__(self):
        self.hitpoint = 20
        self.progress = 0
        self.alive = True

    def attacked(self):
        print('你挥剑向她砍去')
        if self.progress == 0:      #随进度降低旅行者防备你攻击的概率
            weights = [50,50]
        elif self.progress == 1:
            weights = [20,80]
        else:
            weights = [0,100]
        result = random.choices(['cautious','relaxed'],weights=weights)[0]
        print(result)
        if result == 'cautious':
            input('她似乎并没有完全放下对你的戒备,该对此感到欣慰吗')
            input('尽管如此,鲜血还是从她的左臂上流出..')
            input('"你.."')
            Traveler.lose_hitpoint(3)
            fight(Traveler)
        else:
            input('她显然没有想到你会这么做,慌忙向左边闪躲,但已经迟了')
            input('"你.."')
            input('这是你听见她说的最后一句话')
            Traveler.dead()

    def looted(self):
        input('你举起了剑,示意自己不是什么好人')
        input('她显得有些惊慌,但还是做出了防御的姿态')
        fight(Traveler)

    def attack(self,entity):
        attack = random.choices([self.attack1,self.attack2],weights=[70,30])[0]
        attack(entity)
    
    def attack1(self,entity):
        damage =random.randint(4,5)
        if entity == You:
            print('她犹豫着挥动了剑')
            if You.Flag_dodge == True:
                if random.randint(1,100) <= You.agile:
                    print('你避开了攻击')
                    damage = 0
                    You.counter_attack(Traveler)
                else:
                    print('你没有想象中的那么敏捷')
            if damage > 0:
                print('红色的鲜血从伤口中流出')
                You.lose_hitpoint(damage)
        if entity == Mud:
            print('旅行者向怪物挥动了剑')
            Mud.lose_hitpoint(damage)
    
    def attack2(self,entity):
        damage =random.randint(6,8)
        if entity == You:
            print('她轻声吟唱着什么..火焰随之升腾而起')
            if You.Flag_dodge == True and entity == You:
                if random.randint(1,100) <= You.agile:
                    print('你躲过了她的火焰')
                    damage = 0
                    You.counter_attack(Traveler)
                else:
                    print('你没有想象中的那么敏捷')
            if damage > 0:
                print('火焰灼烧着你的身体')
                You.lose_hitpoint(damage)
        if entity == Mud:
            print('旅行者轻声吟唱着什么..火焰随之升腾而起')
            Mud.lose_hitpoint(damage)
    
    def dodge(self,damage):
        result = random.randint(1,100)
        if result > You.accuracy:
            print('她躲过了你的攻击')
        else:
            print(f'你造成了{damage}点伤害')
            self.lose_hitpoint(damage)
        
    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()

    def dead(self):
        print_stress('剑穿透了旅行者的身体,你看着她逐渐失去力气,直至那双眼眸也终于不再明亮')
        input('...')
        self.alive = False

class Robber:
    def __init__(self):
        self.hitpoint = 12
        self.default_hitpoint = 12
        self.damage = 4
    
    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功了避开了攻击')
                damage = 0
                You.counter_attack(Robber)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('他的匕首刺伤了你')
            entity.lose_hitpoint(damage)

    def dodge(self,damage):
        result = random.randint(1,100)
        if result > You.accuracy:
            print('他躲过了你的攻击')
        else:
            print(f'你造成了{damage}点伤害')
            self.lose_hitpoint(damage)
    
    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你将剑刺入了他的喉咙')
        if random.randint(1,100) < 70:
            gold = random.randint(1,9)
            You.gold += gold
            print(f'你在尸体上找到了{gold}枚银币')
class Drunkard:
    def __init__(self):
        self.hitpoint = 12
        self.default_hitpoint = 12
        self.damage = 2
    
    def intro(self):
        print('你遇到了一个醉醺醺的酒鬼')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('他挥拳向你打来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile + 20:
                print('你成功了避开了攻击')
                damage = 0
                You.counter_attack(Drunkard)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('你的脸上挨了一拳')
            entity.lose_hitpoint(damage)
    
    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()

    def dead(self):
        print_stress('你将剑刺入了他的喉咙')
        if random.randint(1,100) < 50:
            gold = random.randint(1,5)
            You.gold += gold
            print(f'你从尸体的口袋中摸走了{gold}枚银币')
class Stranger:
    def __init__(self):
        self.hitpoint = 14
        self.default_hitpoint = 14
        self.damage = 3
    
    def attack(self,entity):
        damage = self.damage + random.randint(0,1) #随机伤害修正
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功了避开了攻击')
                damage = 0
                You.counter_attack(Stranger)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('他挥拳打到了你的腹部')
            entity.lose_hitpoint(damage,attacker=Stranger)
    
    def dodge(self,damage):
        result = random.randint(1,100)
        if result > You.accuracy -10:
            print('他躲过了你的攻击')
        else:
            print(f'你造成了{damage}点伤害')
            self.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你将剑刺入了他的喉咙')
        if random.randint(1,100) < 50:
            gold = random.randint(1,7)
            You.gold += gold
            print(f'你从尸体的口袋中摸走了{gold}枚银币')

class Slime:
    def __init__(self):
        self.hitpoint = 12
        self.default_hitpoint = 12
        self.damage = 3
    
    def intro(self):
        print('一团果冻状的生物')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('果冻突然开始攻击你')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Slime)
            else:
                print('你连果冻的攻击都躲不掉..')
        if damage > 0:
            print('果冻对你造成了伤害')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('果冻不再动弹了..')
        You.obtain(Gel)
class Wolf:
    def __init__(self):
        self.hitpoint = 12
        self.default_hitpoint = 12
        self.damage = 5
    
    def intro(self):
        print('一只毛茸茸的狼')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它想尝你一口')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile -10:
                print('你不想给它吃')
                damage = 0
                You.counter_attack(Wolf)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('似乎味道不错:P')
            entity.lose_hitpoint(damage)
    
    def dodge(self,damage):
        result = random.randint(1,100)
        if result > You.accuracy - 10:
            print('它闪开了你的攻击')
        else:
            print(f'你造成了{damage}点伤害')
            self.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它死了,这都怪你太过可口了')
        item = random.choice([Raw_meat,Wolfskin])
        You.obtain(item)
class Insect:
    def __init__(self):
        self.hitpoint = 12
        self.default_hitpoint = 12
        self.damage = 4
    
    def intro(self):
        print('一只巨大的,长翅膀的昆虫')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它亮出了尾部的刺')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Insect)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被刺伤了')
            entity.lose_hitpoint(damage)

    def dodge(self,damage):
        result = random.randint(1,100)
        if result > You.accuracy - 10:
            print('它闪开了你的攻击')
        else:
            print(f'你造成了{damage}点伤害')
            self.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你杀死了巨大飞行昆虫')
class Earth_Elemental:
    def __init__(self):
        self.hitpoint = 20
        self.default_hitpoint = 20
        self.damage = 3
    
    def intro(self):
        print('你听到了大地嗡鸣的声音..它从碎石和泥土中缓缓显现')

    def attack(self,entity):
        damage = self.damage + random.randint(0,2)
        print('巨大的石块凭空漂浮着')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Earth_Elemental)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被袭来的石块击中')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它化为碎石落下')
class Golem:
    def __init__(self):
        self.hitpoint = 35
        self.alive = True
    
    def intro(self):
        print_stress('古老的魔像苏醒了..')

    def attack(self,entity):
        attack = random.choices([self.attack1,self.attack2],weights=[70,30])[0]
        attack(entity)

    def attack1(self,entity):
        damage = random.randint(4,6)
        print('它挥动沉重的石杖')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile +15:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Golem)
            else:
                print('你没能避开攻击')
        if damage > 0:
            print('你被击中了')
            entity.lose_hitpoint(damage)
    
    def attack2(self,entity):
        damage = random.randint(7,9)
        print('它的左眼涌动着魔力的光辉..')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Golem)
            else:
                print('你被击中了')
        if damage > 0:
            print('毁灭的光束击中了你')
            entity.lose_hitpoint(damage)
        
    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它沉重的身躯缓缓倒下..')
        self.alive = False

class Crocodile:
    def __init__(self):
        self.hitpoint = 15
        self.default_hitpoint = 15
        self.damage = 5
    
    def intro(self):
        print('沼泽下的捕食者盯上了你')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('鳄鱼向你扑咬而来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Crocodile)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被鳄鱼咬了一口')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你杀死了这只鳄鱼')
        item = random.choice([Raw_meat,Crocodlie_skin])
        You.obtain(item)
class Skeleton:
    def __init__(self):
        self.hitpoint = 15
        self.default_hitpoint = 15
        self.damage = 4
    
    def intro(self):
        print_stress('一具骷髅..血肉已消失不见,唯余白骨')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('骷髅挥舞着刀向你袭来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Skeleton)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被砍伤了')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('再一次,化为白骨')
        You.obtain(Bone)
class Corpse:
    def __init__(self):
        self.hitpoint = 15
        self.default_hitpoint = 15
        self.damage = 3
    
    def intro(self):
        print_stress('死尸,但似乎死的不太完全')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它嘶哑的叫喊着什么,向你冲来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Corpse)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被它扑倒撕咬着')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('')
class Mud:
    def __init__(self):
        self.hitpoint = 30
        self.damage = 7

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('...')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Mud)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('它腐蚀着你的身体')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它沉入了沼泽之中..')
class Tentacle:
    def __init__(self):
        self.hitpoint = 17
        self.default_hitpoint = 17
        self.damage = 5
    
    def intro(self):
        print('你感到有什么东西缠上了你的脚腕')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('触手向你拍击而来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Tentacle)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('你被击中了')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它死了')
class Death_Knight:
    def __init__(self):
        self.hitpoint = 30
        self.damage = 8
        self.alive = True
    
    def intro(self):
        print_stress('于黑泥中腐烂的骑士..却依然紧握着它的剑')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它挥剑向你砍去')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Death_Knight)
            else:
                print('你没能避开攻击')
        if damage > 0:
            entity.lose_hitpoint(damage)
    
    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你战胜了它')
        print_stress('"我要离开这里了,你呢?",你将剑从它的身体中拔出')
        self.alive = False

class Snake:
    def __init__(self):
        self.hitpoint = 10
        self.default_hitpoint = 10
        self.damage = 3
    
    def intro(self):
        print_stress('一条巨大的python!呃,我是说..蟒蛇')
        print_stress('它吐出信子,发出嘶嘶的声音')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它突然发动了袭击')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile -10:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Snake)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被咬中了')
            You.status('poison',3,3)
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你将它砍死了')

    pass
class Spider:
    def __init__(self):
        self.hitpoint = 15
        self.default_hitpoint = 15
        self.damage = 4
    
    def intro(self):
        print_stress('你从来没有见过这么大的蜘蛛')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它向你发动了袭击')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile -10:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Spider)
            else:
                print('你没有躲过这次攻击')
        if damage > 0:
            print('你被咬中了')
            You.status('poison',3,3)
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('你将它砍死了')
class Bear:
    def __init__(self):
        self.hitpoint = 25
        self.default_hitpoint = 25
        self.damage = 5
    
    def intro(self):
        print('这是一只熊')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它想要和你来一个拥抱')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Bear)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('有些疼..但你有什么理由拒绝一个拥抱呢?')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它死了')
        item = random.choice([Raw_meat,Bearpaw])
        You.obtain(item)
class Fairy:
    def __init__(self):
        self.hitpoint = 20
        self.default_hitpoint = 20
        self.damage = 4
    
    def intro(self):
        print('精灵..?或是什么其它的生物..')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('它看起来对你不是很友好')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Fairy)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('你忽然感到身体传来剧烈的疼痛')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它死了')
class Dryad:
    def __init__(self):
        self.hitpoint = 18
        self.default_hitpoint = 18
        self.damage = 4
    
    def intro(self):
        print('眼前的树蔓仿佛有生命一般扭动着..')

    def attack(self,entity):
        damage = self.damage + random.randint(-1,1)
        print('藤蔓向你拍击而来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你成功避开了攻击')
                damage = 0
                You.counter_attack(Dryad)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('你被击中了')
            entity.lose_hitpoint(damage)

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()
            
    def dead(self):
        print_stress('它死了')
class Witch:
    def __init__(self):
        self.hitpoint = 30
        self.progress = 0

    def attack(self,entity):
            attack = random.choices([self.attack1,self.attack2],weights=[70,30])[0]
            attack(entity)

    def attack1(self,entity):
        damage =random.randint(4,7)
        print('她用汤勺敲了敲你的头')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你避开了攻击')
                damage = 0
                You.counter_attack(Witch)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('你被敲的眼冒金星')
            You.lose_hitpoint(damage,attacker=Witch)

    def attack2(self,entity):
        print('她念叨着奇怪的咒语')
        You.status('weak',3,3)
    
    def dodge(self,damage):
        result = random.randint(1,100)
        if result > You.accuracy:
            print('她躲过了你的攻击')
        else:
            print(f'你造成了{damage}点伤害')
            self.lose_hitpoint(damage)
        
    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        if self.hitpoint <= 0:
            self.dead()

    def dead(self):
        print_stress('你击败了她')
        You.obtain(Strange_Potion)
        You.obtain(Strange_Potion)
        You.obtain(Strange_Potion)
        You.obtain(Strange_Potion)
class The_Big_Bad_Wolf:
    def __init__(self):
        self.hitpoint = 40
        self.damage = 5
        self.alive = True

    def intro(self):
        print('这是一只很大可能也很坏的狼')

    def attack(self,entity):
        attack = random.choices([self.attack1,self.howl],weights=[70,30])[0]
        attack(entity)

    def attack1(self,entity):
        damage = self.damage + random.randint(-1,1)
        print_stress('很大可能也很坏的狼向你冲来')
        if You.Flag_dodge == True:
            if random.randint(1,100) <= You.agile:
                print('你避开了攻击')
                damage = 0
                You.counter_attack(The_Big_Bad_Wolf)
            else:
                print('你没有想象中的那么敏捷')
        if damage > 0:
            print('红色的鲜血从你的身体中流出')
            entity.lose_hitpoint(damage)

    def howl(self,entity): #需要接收entity参数，尽管在howl方法中用不到，否则会报错
        print('很大可能也很坏的狼仰天长啸')
        print_stress('嗷呜~')
        self.damage += 1

    def lose_hitpoint(self,hurt):
        self.hitpoint -= hurt
        print(hurt)
        if self.hitpoint <= 0:
            self.dead()
        
    def dead(self):
        print_stress('这是一只很大但现在可能已经死了的狼')
        self.alive = False


#Item
class Angel:
    def __init__(self):
        self.name = '?'
        self.space = 1
        self.price = 99
    
    def intro(self):
        print_stress('白色天使')

    def use(self):
        You.status('Angel',0,3)
        input('你与我同在')
        You.backpack.remove(self)
    
    def effect(self):
        You.get_angel = True #判断你有没有获得过angel,暂时还没用上

class Red_Gem:
    def __init__(self):
        self.name = '红色宝石'
        self.space = 1
        self.price = 50

    def intro(self):
        print_stress('你从中感到了心')
    
    def effect(self):
        You.max_hitpoint = 40

    def del_effect(self):
        You.max_hitpoint = 30
class Air_Gem:
    def __init__(self):
        self.name = '透明宝石'
        self.space = 1
        self.price = 50
        self.ability = False

    def intro(self):
        print_stress('你感到身体变得轻盈')
    
    def effect(self):
        You.agile = 45
        self.ability = True

    def del_effect(self):
        You.agile = 30
        self.ability = False
class Yellow_Gem:
    def __init__(self):
        self.name = '黄色宝石'
        self.space = 1
        self.price = 50

    def intro(self):
        print_stress('你从中感受到了力量')
    
    def effect(self):
        You.attack_damage = 7
    
    def del_effect(self):
        You.attack_damage = 5

class Healing_Potion:
    def __init__(self):
        self.name = '治疗药水'
        self.space = 5
        self.price = 10
    
    def intro(self):
        print_stress('一瓶暖红色的药水')

    def use(self):
        You.heal(10)
        input('你喝下了治疗药水')
        You.backpack.remove(self)
class Strength_Potion:
    def __init__(self):
        self.name = '力量药水'
        self.space = 5
        self.price = 10
    
    def intro(self):
        print_stress('一瓶淡黄色的药水')

    def use(self):
        You.status('strength',3,5)
        input('你喝下了力量药水')
        You.backpack.remove(self)   
class Agile_potion:
    def __init__(self):
        self.name = '灵巧药水'
        self.space = 5
        self.price = 10

    def intro(self):
        print_stress('一瓶淡白色的药水')

    def use(self):
        You.status('agile',15,3)
        input('你喝下了灵巧药水')
        You.backpack.remove(self) 
class Strange_Potion:
    def __init__(self):
        self.name = '奇怪的药水'
        self.space = 5
        self.price = 10
    
    def intro(self):
        print_stress('一瓶奇怪的的药水')

    def use(self):
        input('你喝下了药水')
        result = random.choice(['heal','poison','strength','agile'])
        if result == 'heal':
            You.heal(10)
        elif result == 'poison':
            You.status('poison',3,3)
        elif result == 'strength':
            You.status('strength',4,4)
        elif result == 'agile':
            You.status('agile',15,4)
        You.backpack.remove(self)
class Antidote:
    def __init__(self):
        self.name = '解毒药水'
        self.space = 5
        self.price = 10
        self.used = False

    def intro(self):
        print_stress('一瓶淡绿色的药水')

    def use(self):
        self.used = True
        You.status_check()
        self.used = False
        input('你喝下了解毒药水')
        You.backpack.remove(self) 

class Food:
    def __init__(self,name,value,space,price):
        self.name = name
        self.value = value
        self.space =space
        self.price =price

    def intro(self):
        print(f'一个{self.name}')

    def eat(self):
        input(f'你吃下了{self.name}')
        You.eat(self.value)
        if self == Raw_meat:
            print('不太好吃...')
            result = random.randint(1,100)
            if result <= 25:
                You.status('poison',3,3)
        You.backpack.remove(self)
Apple = Food('苹果',6,2,3) #Food(名称,饱腹值,占用空间,价格)
Cheese = Food('奶酪',10,2,5)
Meat = Food('肉干',20,5,8)
Bread = Food('面包',10,2,5)
Muffin = Food('松饼',10,2,5)
Sausage = Food('香肠',10,2,5)
Candy = Food('糖果',3,1,2)
Cat_Cookie = Food('咸味小猫饼干',5,1,3)
Raw_meat = Food('生肉',11,4,6)


class Item:
    def __init__(self,name,space,price):
        self.name = name
        self.space =space
        self.price =price
    
    def intro(self):
        print(f'{self.name}')
Gel = Item('凝胶',3,5) #Item(名称,占用空间,价格)
Wolfskin = Item('狼皮',5,10)
Bone = Item('骨头',5,15)
Bearpaw = Item('熊掌',5,20)
Crocodlie_skin = Item('鳄鱼皮',5,18)


   

#实例化
Angel = Angel()
You = You()
Dragon = Dragon()
Traveler = Traveler()
Robber = Robber()
Drunkard = Drunkard()
Stranger = Stranger()
Slime = Slime()
Wolf = Wolf()
Insect = Insect()
Earth_Elemental = Earth_Elemental()
Golem = Golem()
Crocodile = Crocodile()
Skeleton = Skeleton()
Corpse = Corpse()
Mud = Mud()
Tentacle = Tentacle()
Death_Knight = Death_Knight()
Snake = Snake()
Bear = Bear()
Spider = Spider()
Fairy = Fairy()
Dryad = Dryad()
Witch = Witch()
The_Big_Bad_Wolf = The_Big_Bad_Wolf()
Red_Gem = Red_Gem()
Air_Gem = Air_Gem()
Yellow_Gem = Yellow_Gem()
Healing_Potion = Healing_Potion()
Strength_Potion = Strength_Potion()
Agile_potion = Agile_potion()
Strange_Potion = Strange_Potion()
Antidote = Antidote()


#Map
class town:
    def action(self):
        print_stress('你在城镇中,街道两旁是古老的石砌建筑,散发着安心的气息。')
        if sys.day: #如果是白天
            print('1.启程\n2.前往集市\n3.前往酒馆\n4.前往码头\n5.随便逛逛\n6.打开背包\n7.休息') #显示行动选项
            choice = input_('你选择..?\n',[1,7]) #获取你的选择,赋值给choice
            if choice == 1:
                input('你走在白日喧闹的街道上')
                sys.step += random.randint(3,5) #增加路程
                town.event() #随机触发事件
            elif choice ==2:
                print('你前往集市')
                market()
            elif choice ==3:
                print('你走进酒馆')
                tavern()
            elif choice ==4:
                print('你来到了码头,海鸥大摇大摆的四处走着')
                dock()
            elif choice ==5:
                town.event()
            elif choice == 6:
                print('你打开了背包') #查看背包不会导致时间和饥饿值的流逝
                sys.round -= 1
                sys.time -= 1
                You.hunger += 1.5
                You.open_backpack()
                Game()
            elif choice ==7:
                You.rest()

        elif sys.night:
            print('1.启程\n2.前往酒馆\n3.随便逛逛\n4.打开背包\n5.休息')
            choice = input_('你选择..?\n',[1,5])
            if choice == 1:
                input('你走在夜晚安静的街道上')
                sys.step += random.randint(1,3)
                town.event()
            elif choice == 2:
                tavern()
            elif choice ==3:
                town.event()
            elif choice == 4:
                sys.round -= 1
                sys.time -= 1
                You.hunger += 1.5
                print('你打开了背包')
                You.open_backpack()
                Game()
            elif choice ==5:
                You.rest()

    def event(self):
        if sys.day:
            event = random.choices(['peace',fight,robber,strange,begger],weights=[80,5,5,5,5])[0]
        if sys.night:
            event = random.choices(['peace',fight,robber,strange,begger],weights=[60,13.3,13.3,13.3,0])[0]
        if event == 'peace':
            pass
        elif event == fight:
            entity = random.choices([Drunkard],weights=[100])[0]
            fight(entity)
        else:
            event()
        Game()

class plains:

    def action(self):
        print_colored('你在宁静的碧绿色平原上',Fore.GREEN)
        if sys.day:
            print('1.向北前行\n2.向南前行\n3.在平原上散步\n4.打开背包\n5.休息')
            choice = input_('你选择..?\n',[1,5])
            if choice == 1:
                input('你漫步在广阔的碧绿色平原上,微风从远方吹拂而来')
                sys.step += random.randint(1,4)
                plains.event() 
            elif choice == 2:
                sys.step -= random.randint(2,4)
                plains.event()
            elif choice == 3:
                plains.event()
            elif choice == 4:
                sys.round -= 1
                sys.time -= 1
                You.hunger += 1.5
                print('你打开了背包')
                You.open_backpack()
                Game()
            elif choice == 5:
                You.rest()
        elif sys.night:
            print('1.向北前行\n2.向南前行\n3.在平原上散步\n4.打开背包\n5.休息')
            choice = input_('你选择..?\n',[1,5])
            if choice == 1:
                input('你在夜色中的碧绿色平原上前行')
                sys.step += random.randint(0,3)
                plains.event() 
            elif choice == 2:
                sys.step -= random.randint(1,3)
                plains.event()
            elif choice == 3:
                plains.event()
            elif choice == 4:
                sys.round -= 1
                sys.time -= 1
                You.hunger += 1.5
                print('你打开了背包')
                You.open_backpack()
                Game()
            elif choice == 5:
                You.rest()
            
    def event(self):
        if sys.day:
            event = random.choices(['peace','traveler','fight',treasure,hunting],weights=[30,10,30,15,15])[0]
        if sys.night:
            event = random.choices(['peace','traveler','fight',treasure,hunting],weights=[50,0,30,10,10])[0]
        if event == 'peace':
            pass
        elif event == 'fight':
            entity = random.choices([Slime,Wolf,Insect,Earth_Elemental],weights=[35,30,20,15])[0]
            fight(entity)
        elif event == 'traveler' and Traveler.alive:
            if Traveler.progress == 0:
                traveler1()
            elif Traveler.progress == 1:
                traveler2()
        else:
            event()
        Game()

class swamp:
    if Air_Gem.ability:
        You.deep += random.randint(0,1)
    else:
        You.deep += random.randint(0,2)
       
    def action(self):
        print_stress('你在潮湿的沼泽中,空气弥漫着腐烂的气息')
        if sys.day:
            print('1.向北前行\n2.向南前行\n3.探索沼泽\n4.打开背包\n5.休息')
            choice = input_('你选择..?\n',[1,5])
            if choice == 1:
                input('你在泥泞的沼泽地中勉强前行')
                sys.step += random.randint(0,3)
                swamp.event()
            elif choice == 2:
                sys.step -= random.randint(0,3)
            elif choice == 3:
                swamp.event()
            elif choice == 4:
                sys.round -= 1
                sys.time -= 1
                You.hunger += 1.5
                print('你打开了背包')
                You.open_backpack()
                Game()
            elif choice == 5:
                if You.deep < 20:
                    if random.randint(1,2) == 1:
                        You.rest()
                    else:
                        print('你没能在泥潭中找到可以休息的地方..')
                elif You.deep >= 20:
                    print('你在原地站着休息了一会...')

        elif sys.night:
            print('1.向北前行\n2.向南前行\n3.探索沼泽\n4.打开背包\n5.休息')
            choice = input_('你选择..?\n',[1,5])
            if choice == 1:
                input('你在泥泞的沼泽地中勉强前行')
                sys.step += random.randint(-1,3)
                swamp.event()
            elif choice == 2:
                sys.step -= random.randint(-1,3)
            elif choice == 3:
                swamp.event()
            elif choice == 4:
                sys.round -= 1
                sys.time -= 1
                You.hunger += 1.5
                print('你打开了背包')
                You.open_backpack()
            elif choice == 5:
                if You.deep < 20:
                    if random.randint(1,2) == 1:
                        You.rest()
                    else:
                        print('你没能在泥潭中找到可以休息的地方..')
                elif You.deep >= 20:
                    print('你在原地站着休息了一会...')

    def event(self):
        if sys.day:
            event = random.choices(['peace','traveler','fight',treasure,corpse],weights=[30,10,30,15,15])[0]
        if sys.night:
            event = random.choices(['peace','traveler','fight',treasure,corpse],weights=[50,0,30,10,10])[0]
        if event == 'peace':
            pass
        elif event == 'fight':
            entity = random.choices([Crocodile,Corpse,Skeleton,Tentacle],weights=[25,25,25,25])[0]
            fight(entity)
        elif event == 'traveler' and Traveler.alive:
            if Traveler.progress == 2:
                traveler3()
        else:
            event()
        Game()

class forest:
    def action(self):
        print_colored('你在黑暗的森林中,高耸的树木遮蔽了阳光',Fore.GREEN)
        print('1.向北?前行\n2.向南?前行\n3.探索森林\n4.打开背包\n5.休息')
        choice = input_('你选择..?\n',[1,5])
        if choice == 1:
            input('你在无光的森林试图前行')
            sys.step += random.randint(-1,3)
            forest.event()
        elif choice == 2:
            sys.step -= random.randint(-3,1)
        elif choice == 3:
            forest.event()
        elif choice == 4:
            sys.round -= 1
            sys.time -= 1
            You.hunger += 1.5
            print('你打开了背包')
            You.open_backpack()
            Game()
        elif choice == 5:
            You.rest()

    def event(self):
        event = random.choices(['peace','fight',treasure,witch],weights=[30,30,15,15])[0]
        if event == 'peace':
            pass
        elif event == 'fight':
            entity = random.choices([Bear,Spider,Fairy,Snake,Dryad],weights=[20,20,20,20,20])[0]
            fight(entity)
        else:
            event()
        Game()

class mountain:
    def action(self):
        input('你来到了连绵的山脉上,据说巨龙就栖息在前面不远处的山洞中')
        print('1.前往\n2.后退\n3.休息')
        choice = input_('你选择..?\n',[1,3])
        if choice == 1:
            print('你向前走去')
            fight(Dragon)
        elif choice == 2:
            sys.step -= random.randint(-3,0)
        elif choice == 3:
            You.rest()

town = town()
plains = plains()
swamp = swamp()
forest = forest()
mountain = mountain()


#Event
def market():
    print(f'你的银币:{You.gold}')
    print('你来到了熙攘的集市之中,商贩们的摊子上摆满了宝石,魔药,食物..')
    print('1.随便看看\n2.出售物品\n3.离开集市')
    choice = input_('你选择..?\n',[1,3])
    if choice == 1: #购买物品
        print('你来到一个商贩面前,看了看商品')
        store = [Apple,Cheese,Meat,Bread,Muffin,Sausage,Candy,Cat_Cookie,Healing_Potion,Strength_Potion,Agile_potion,Strange_Potion,Antidote,Red_Gem,Air_Gem,Yellow_Gem,Angel] #创建商店物品列表
        goods_weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.1] #设置不同物品出现的权重
        list_goods = random.choices(store,weights=goods_weights,k=5) #从可售卖的物品中按照权重随机选择5个出售,返回列表
        while True: 
            sys.time += 0.5
            You.hungry(0.5)
            print(f'你的银币:{You.gold}')
            number = 0
            print('0.离开摊位')
            for item in list_goods:
                number += 1
                print(f'{number}.{item.name} ({item.price}银币)')
            choice = input_('你选择..?\n',[0,number])
            if choice == 0:
                market()
                return #在调用自身时结束本次进程(保险起见)
            else:
                choice -= 1
                goods = list_goods[choice] #以goods表示被选中的商品
                goods.intro() #介绍被选中的商品
                print('1.购买\n2.放下')
                choice = input_('你选择..?\n',[1,2])
                if choice == 1:
                    print(choice)
                    if not You.pay(goods.price): #如果你没有足够的钱
                        continue 
                    You.obtain(goods)
                    list_goods.remove(goods)
                elif choice == 2:
                    print(f'你放下了{goods.name}')
                continue
    elif choice == 2: #出售物品
        print('你在垃圾桶旁边找了一块看起来还算干净的布,把它铺到了地上')
        print('你放下背包,准备把东西拿出来售卖')
        list_goods = [] #你的商品列表
        while True: #循环 从背包中选择要出售的物品
            print('0.关上背包')
            number = 0 
            for item in You.backpack:  #遍历背包
                number += 1
                print(f'{number}.{item.name}')
            choice = input_('你选择..?\n',[0,number])
            if choice == 0:
                print('你关上了背包')
                break
            elif choice != 0: #如果选择了对应的物品
                choice -= 1 
                print(f'你将{You.backpack[choice].name}从背包取了出来')
                list_goods.append(You.backpack[choice]) #添加物品到商品列表
                You.backpack.pop(choice) #从背包中移除该物品
                continue
        if not list_goods:
            market()
            return
        while list_goods: #当商品列表不为空
            sys.time += 0.5
            You.hungry(0.5)
            result = random.choices(['nothing','customer'],weights=[50,50])[0] #随机判定是否有人对你的商品感兴趣
            if result == 'nothing':
                print('无人在意你的商品..')
            elif result == 'customer': #如果有人对你的商品感兴趣
                demand = random.choice(list_goods) #从你的商品列表中随机选择一个物品作为顾客想要的
                price = demand.price #基础价格等于该物品的价格
                add_price = random.randint(0,price//5) #随机额外价格,最多为该物品原价的20%
                max_price = price + add_price #客人最多愿意付出的金额为基础价格+额外价格
                gender = random.choice(['他','她']) #随机客人性别
                print(f'有人似乎对你的{demand.name}起了兴趣')
                print_stress(f'我可以出{price}个银币')
                print('1.同意\n2.抬价\n3.拒绝')
                choice = input_('你选择..?\n',[1,3])
                if choice == 1:
                    print('你同意了这笔交易')
                    list_goods.remove(demand)
                    if hasattr(item,'effect'):
                        demand.del_effect()
                    print(f'你获得了{price}枚银币')
                    You.gold += price
                elif choice == 2:
                    expect = input_('你给出的价格是..?\n',[0,999])
                    if expect <= max_price:
                        print(f'{gender}同意了')
                        list_goods.remove(demand)
                        print(f'你获得了{expect}枚银币')
                        You.gold += expect
                    elif expect > max_price:
                        print(f'{gender}拒绝了你的出价')
                elif choice == 3:
                    print('你拒绝了这笔交易')
            print('1.继续\n2.收摊')
            choice = input_('你选择..?\n',[1,2])
            if choice == 1:
                if list_goods:
                    continue
                if not list_goods:
                    input('你的商品全部卖出去了')
                    market()
                    return
            elif choice ==2:
                print('你将东西收好,起身离开')
                for item in list_goods:
                    You.backpack.append(item)
                market()
                return
    elif choice == 3:
        print('你离开了集市')
    Game()

def tavern():
    while True:
        print('1.喝酒\n2.吃东西\n3.离开')
        choice = input_('你选择..?\n',[1,3])
        if choice == 1:
            print('1.啤酒 (5银币)\n2.葡萄酒 (10银币)\n3.苹果酒 (10银币)\n4.蜂蜜酒 (10银币)\n5.浆果汁 (8银币)\n6.再想一下')
            choice = input_('你选择..?\n',[1,6])
            sys.time += 1
            if choice == 1:
                print('你点了一杯啤酒')
                if not You.pay(5):
                    continue
                You.drink(7)
            elif choice == 2:
                print('你点了一杯葡萄酒')
                if not You.pay(10):
                    continue
                You.drink(15)
            elif choice == 3:
                print('你点了一杯苹果酒')
                if not You.pay(10):
                    continue
                You.drink(15)
            elif choice == 4:
                print('你点了一杯蜂蜜酒')
                if not You.pay(10):
                    continue
                You.drink(15)
            elif choice == 5:
                if not You.pay(8):
                    continue
                print('你点了一杯浆果汁')
                input('喝浆果汁')
                input('喝..')
            elif choice == 6:
                print('你决定再想想')
                sys.time -= 1
            continue
        elif choice == 2:  #弓箭型代码:P
            print('1.苹果派 (6银币)\n2.果仁蜜饼 (8银币)\n3.麦片粥 (5银币)\n4.蔬菜杂烩 (10银币)\n5.烤鱼 (15银币)\n6.烤野兔 (15银币)\n7.烤羊腿 (20银币)\n8.炖肉 (18银币)\n9.再想一下')
            choice = input_('你选择..?\n',[1,9])
            sys.time += 1
            if choice == 1:
                print('你点了一个苹果派')
                if not You.pay(6):
                    continue
                You.eat(10)
            elif choice == 2:
                print('你点了一个果仁蜜饼')
                if not You.pay(8):
                    continue
                You.eat(12)
            elif choice == 3:
                print('你点了一碗麦片粥')
                if not You.pay(5):
                    continue
                You.eat(10)
            elif choice == 4:
                print('你点了一碗蔬菜杂烩')
                if not You.pay(10):
                    continue
                You.eat(12)
            elif choice == 5:
                print('你点了一只烤鱼')
                if not You.pay(15):
                    continue
                You.eat(20)
            elif choice == 6:
                print('你点了一只烤野兔')
                if not You.pay(15):
                    continue
                You.eat(18)
            elif choice == 7:
                print('你点了一个烤羊腿')
                if not You.pay(20):
                    continue
                You.eat(20)
            elif choice == 8:
                print('你点了一碗炖肉')
                if not You.pay(18):
                    continue
                You.eat(20)
            elif choice == 9:
                print('你决定再想想')
                sys.time -= 1
            continue
        elif choice == 3:
            print('你离开了酒馆')
            break
    Game()

def dock():
    print('1.坐船返回\n2.离开码头')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        print('你望向海面,思考自己是否真的应该放弃拯救公主,坐船回家')
        print('1.是的\n2.不是')
        choice = input_('你选择..?\n',[1,2])
        if choice == 1:
            if not You.pay(30):
                print('船票需要30枚银币..')
                dock()
                return
            print('你付给水手30枚银币,坐上了返程的船')
            sys.Ending4()
        elif choice == 2:
            dock()
            return
    elif choice == 2:
        Game()

def treasure():
    print_stress('你发现了一个半埋在泥土中的宝箱')
    result = random.choices(['just gold','gold and treasure','double treasure'],weights=[25,50,25])[0]
    gold = random.randint(10,30)
    inventory = [Healing_Potion,Strength_Potion,Agile_potion,Strange_Potion,Red_Gem,Air_Gem,Yellow_Gem,Angel]
    treasure = random.choices(inventory,weights=[17.5,17.5,17.5,17.5,9.67,9.67,9.67,1])[0]

    if result == 'just gold':
        You.gold += gold

    elif result == 'gold and treasure':
        You.gold += gold
        You.obtain(treasure)

    elif result == 'double treasure':
        You.gold += gold
        You.obtain(treasure)
        treasure2 = random.choices(inventory,weights=[17.5,17.5,17.5,17.5,9.67,9.67,9.67,1])[0]
        You.obtain(treasure2)

    print(f'你获得了{gold}枚银币')
    input('')
    
def begger():
    print('一个乞丐期待着什么')
    print('1.施舍钱财\n2.施舍食物\n3.无视\n4.拿走乞丐碗里的银币')
    choice = input_('你选择..?\n',[1,4])
    if choice == 1:
        input('你往她面前扔了几个银币')
        You.gold -= 3
    elif choice == 2:
        number = 0
        list = []
        for item in You.backpack:
            if isinstance(item,Food):
                number += 1
                print(f'{number}.{item.name}')
                list.append(item)
        choice = input_('你选择..?',[1,number])
        choice -= 1
        You.backpack.remove(list[choice])
        input(f'你给了她一个{list[choice].name}')
    elif choice == 3:
        input('你没有怜悯她')
    elif choice == 4:
        input('你笑着从她碗中拿走了一枚银币')
        You.gold += 1

def robber():
    print('一个拿着匕首的家伙挡在了你的面前')
    print('"喂,借点钱给哥们花花呗"')
    print('1.同意\n2.拒绝')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        if You.gold >= 5:  #如果你有至少5块钱
            You.gold -= 20 #被抢走了20块
            if You.gold < 0: #如果-20后余额是负数
                You.gold = 0 #重置余额为0
            print('嘿!算你小子识相')
            print('他满意的离开了')
        elif You.gold <5:
            print('"就这点?捡个碗去街上当乞丐吧"')
            print('他呸了一声,往你头上来了一拳')
            You.lose_hitpoint(1)
    elif choice == 2:
        print('他亮了亮手中泛着寒光的匕首:"那就别怪我不客气了"')
        fight(Robber)

def strange():
    print('一个陌生人挡在了你的面前')
    print('小家伙，陪大爷们找些乐子怎么样?')
    print('1.拒绝\n2.拒绝')
    input('你选择..?\n')
    print('陌生人笑了笑:"看来要先好好教训你一下了"')
    fight(Stranger)

def hunting():
    print('你见到一只兔子在平原上吃青草')
    print('1.试图打猎\n2.无视')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        result = random.choices(['success','failure'],weights=[You.agile + 20,50 + (30 - You.agile)])[0]
        if result == 'success':
            print('你杀死了兔子,饱餐了一顿')
            You.eat(15)
        elif result == 'failure':
            print('你没能抓住这只兔子')
    elif choice == 2:
        print('你没有兴致在其它事情上浪费时间')
    
def traveler1():
    input('你望见前方有一个身影,似乎是一位旅行者')
    print('1.前往\n2.无视')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        input('你向旅行者走去,她注意到了你')
        input('"你好啊!",她微笑着向你打招呼')
        print('1.问好\n2.抢夺\n3.攻击')
        choice = input_('你选择..?\n',[1,3])
        if choice == 1:
            input('你笑了笑:"你好"')
            input('她有些疑惑的打量着你,"你也是来旅行的吗?"')
            input('啊,这里的风景真的很好,很适合旅行')
            input('我有时喜欢躺在草地上,什么都不做,就只是看着蓝天..白云..')
            input('虽然有些会攻击人的魔物,不过对付起来都还好啦')
            input('你应该比我厉害许多吧,不过也不能掉以轻心哦')
            input('毕竟那往往意味着..')
            input('她望向远方,没有再继续说下去')
            input('\n你们继续同行了一段时间')
            Traveler.progress = 1
        elif choice == 2:
            Traveler.looted()
        elif choice ==3:
            Traveler.attacked()
    elif choice == 2:
        input('你没有兴致在其它事情上浪费时间')

def traveler2():
    #共同探索平原遗迹
    input('你望见前方有一位熟悉的身影')
    print('1.前往\n2.无视')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        input('你向她走去')
        input('"是你呀!",她似乎很高兴再次遇见你')
        print('1.问好\n2.抢夺\n3.攻击')
        choice = input_('你选择..?\n',[1,3])
        if choice == 1:
            input('你笑了笑:"你好"')
            input('"我听说这附近有一个遗迹",她的眼中暗藏着几分期待')
            input('"想一起去看看吗?"')
            print('1.同意\n2.拒绝')
            choice = input_('你选择..?\n',[1,2])
            if choice == 1:
                input('你和她一起漫步在平原上,寻找传闻中的古老遗迹')
                input('...')
                input('你们找到了遗迹')
                input('早已破败的遗迹中杂草丛生,残垣间散发着沉重的气息')
                input('"呃呃..你觉得这里真的会有宝物吗?"')
                print('1.不会\n2.不会')
                input_('..?\n',[1,2])
                input('你摇了摇头,表示自己对此不抱什么期望')
                input('旅行者:TwT')
                input('你们小心的在遗迹中探索着')
                input('...')
                input('你发现了一个不寻常的雕像,上面刻着神秘的符文')
                input('"W.M.O.E..好像要将它们按照正确的顺序排列.."')
                count = 0
                while True:
                    answer = input('请输入你的答案..\n').upper() #upper方法将所有输入字母转化为大写
                    answer = answer.split(' ') #split方法将answer以空格为界限切割为不同的元素,返回列表
                    answer = ''.join(answer) #join方法将切割后的所有列表元素连接在一起
                    #以上字符串操作使输入中包含小写字母以及空格时同样可以识别成功
                    if answer == 'MEOW':
                        break
                    else:
                        count += 1
                        print('好像没有反应')
                        if count == 5:
                            print('"嗯..我来试试吧",旅行者走到了石像前')
                            break
                        continue
                input('雕像的眼睛发出刺眼的光芒,随后一个宝箱展现在你们的面前')
                input('"啊啊是宝箱!"')
                input('她兴奋的打开了宝箱')
                input('...')
                input('...')
                input('...')
                input('宝箱中装着超级多小猫饼干!')
                input('旅行者:"ww怎么会有这么多小猫饼干!!"')
                input('你:^_^')
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                You.obtain(Cat_Cookie)
                input('你们瓜分了宝箱中的小猫饼干,随后离开了遗迹')
                input('...')
                input('你和她一起躺在草地上,吃着小猫饼干,聊天')
                input('不知不觉间已近傍晚')
                input('金色的夕阳光辉洒在画一般的世界中')
                input('...')
                sys.time = 18
                Traveler.progress = 2
            elif choice == 2:
                input('"啊..好吧",她显得有些失落')
                input('你们继续聊了一会,随后她起身离开了')
        elif choice == 2:
            Traveler.looted()
        elif choice == 3:
            Traveler.attacked()
    elif choice == 2:
        input('你没有兴致在其它事情上浪费时间')
    
def traveler3():
    input('你听见了远处好像传来了奇怪的声音')
    print('1.前往\n2.无视')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        input('你向声音传来的方向走去')
        input('...')
        input('你见到旅行者正在被一个烂泥般的巨大怪物攻击')
        print('1.走近\n2.只是看着\n3.离开\n')
        choice = input_('你选择..?\n',[1,3])
        if choice == 1:
            input('啊..是你')
            input('你向她笑了一下,随后拿起了自己的剑')
            print('1.攻击怪物\n2.攻击旅行者\n')
            choice = input_('你选择..?\n',[1,2])
            if choice == 1:
                fight(Mud)
                if Mud.hitpoint <= 0: #你和旅行者战胜了怪物
                    input('...')
                    input('你陪着旅行者离开了沼泽')
                    input('你们再一次走在了微风吹拂的平原上')
                    input('她好像说了很多,关于自己,也关于你')
                    input('她说很喜欢这里的平原,喜欢这里的蓝天和白云')
                    input('她说非常感谢你的帮助')
                    input('她说继续前行太危险,所以要去其他地方了')
                    input('你听着她的声音,看向远处天空与原野的交界出神')
                    input('最后,她望向你')
                    input('想和我去远方吗?')
                    print('1.好\n2.不好\n')
                    choice = input_('你选择..?\n',[1,2])
                    if choice == 1:
                        input('你答应了')
                        sys.Ending3 = True
                    elif choice == 2:
                        input('你告诉她自己还有必须完成之事')
                        input('她轻声叹了口气,没有再说话')
                        input('离开前,她递给你一个钱袋,请你一定要收下')
                        input('你照做了,为什么不呢')
                        You.gold += 60
                        input('你们告别了')
                else: #你逃跑了
                    input('身后的声音逐渐平息,你觉得自己大概不会再见到她了')
                    Traveler.alive = False
            elif choice == 2:
                Traveler.attacked()
        elif choice == 2:
            input('你不打算做出什么额外的举动')
            input('旅行者喘息着，似乎逐渐耗尽了体力')
            input('...')
            input('她没有躲过那一次攻击')
            input('很快,旅行者沉闷的惨叫和怪物一起消失在了沼泽中')
            Traveler.alive = False
        elif choice == 3:
            input('你转身离开了这里')
            input('你还有未完成的事情,让自己陷入危险之中不是明智的选择')
            input('身后的声音逐渐平息,你觉得自己大概不会再见到她了')
            Traveler.alive = False
    elif choice == 2:
        input('你没有兴致在其它事情上浪费时间')
        Traveler.alive = False
    
    #swamp, being attacked
    #可以逃跑,但不会触发结局

def corpse():
    input('你发现了一具在泥中腐烂的尸体..')
    print('1.前往\n2.无视')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        input('你向其走去..出于贪婪,或是出于怜悯')
        result = random.randint(1,6)
        if result <= 2:
            input('死去的尸体突然开始攻击你')
            fight(Corpse)
        elif result <= 4:
            input('你在尸体上找到了一些有用的东西')
            gold = random.randint(5,15)
            print(f'你找到了{gold}枚银币')
            treasure = random.choices([Healing_Potion,Strength_Potion,Agile_potion,Strange_Potion],weights=[25,25,25,25])[0]
            You.obtain(treasure)
        elif result <= 6:
            input('这只是一具普通的尸体,你在期待什么呢')

def witch():
    if Witch.progress == 2:
        return
    elif Witch.progress == 1:
        input('你见到前方有一间熟悉的木屋')
    elif Witch.progress == 0:
        input('你见到前方好像有一间小木屋')
    print('1.前往\n2.无视')
    choice = input_('你选择..?\n',[1,2])
    if choice == 1:
        input('你走近木屋')
        input('破旧的木板泛着一丝腐烂的味道')
        input('门虚掩着,里面似乎是一片黑暗')
        print('1.敲门\n2.推门\n3.离开')
        choice = input_('你选择..?\n',[1,3])
        Witch.progress = 1
        if choice == 1:
            input('你很有礼貌,先轻敲了几下门')
            input('...')
            input('没有反应')
            print('2.推门\n3.离开')
            choice = input_('你选择..?\n',[2,3])
        if choice == 2:
            Witch.progress = 2
            input('你推开门,轻轻的走进了屋内')
            input('屋子的中央架着一口巨大的铁锅,似乎仍冒着热气')
            input('几支蜡烛东倒西歪的放在满是蜡迹的桌子上,还有一堆装着古怪液体的瓶罐')
            input('其中一支蜡烛被点燃了,它挣扎着散发着微弱的光芒')
            input('一只手突然放在了你的头上')
            input('"你好呀,小朋友"')
            input('你回过头,一个怪异的女人不知道什么时候出现在了你的背后,正微笑着看着你')
            input('她的神色中透露出一种古怪的稳重')
            input('你后退几步,不小心撞到了那一口巨大的锅')
            input('"啊"')
            input('她轻声叹了口气,从旁边拿起一个..大木勺')
            input('尝尝我煮的汤吧')
            print('1.喝下\n2.不喝\n')
            choice = input_('你选择..?\n',[1,2])
            if choice == 1:
                input('死癞蛤蟆,青蛙内脏和树皮腐烂的味道在你的口腔中共同涌现..')
                You.status('weak',1,10)
                You.status('poison',3,5)
                input('"乖孩子"')
                input('她赞赏般的摸了摸你的头,任由你摇摇晃晃的走出了木屋')
            elif choice == 2:
                input('她看起来有些苦恼')
                input('嗯..真是不听话的孩子')
                input('你握紧了手中的剑..')
                fight(Witch)
        if choice == 3:
            input('你离开了这间奇怪的木屋')
    elif choice == 2:
        input('你没有兴致在其它事情上浪费时间')

class trash:
    pass
    #补充怪物信息
    #完善旅行者支线
    #补充道具信息
    #优化休息机制
    #战利品系统
    #你现在的任务是写完旅行者支线
    #酒馆和集市
    #丢弃or出售物品时 删除被动效果
    #背包容量..(感觉有些复杂，不行的话不做也可以)（按照每个物品占的空间计算？）(写好了)

    #旧版行动
    def action():
        
        print('1.前进\n2.返回\n3.环顾四周\n4.休息')
        choice = input('你选择..?\n')

        if sys.day:
            if choice == '1':
                print('你沿着一条正确的路吗?')
                sys.step += random.randint(-2,5)
                #event()
            elif choice == '2':
                print('你还能指望我什么呢')
                sys.step += random.randint(-5,2)
                if sys.step < 0:
                    sys.Ending2 = True
                    Game()
                    return
            elif choice == '3':
                print('你环顾四周')
            elif choice == '4':
                print('你选择休息一会')

        if sys.night:
            if choice == '1':
                print('你沿着一条正确的路吗?')
                sys.step += random.randint(-4,5)
                #event()
            elif choice == '2':
                print('你还能指望我什么呢')
                sys.step += random.randint(-5,4)
                if sys.step < 0:
                    sys.Ending = True
                    Game()
                    return
            elif choice == '3':
                pass
            elif choice == '4':
                pass
        print(sys.step)
        Game()

    #旧版事件
    def event():
        if sys.place == 'vallage':
            value = random.randint(1,100)
            if value <= 20:
                entity = random.choice(['list_monster_town'])
                fight(entity)
            elif value <= 80:
                pass #平静
            elif value <= 100:
                pass
                # otherevent_town()
        
        if sys.place == 'plain':
            pass

input('很久以前,北方的山脉中栖息着一只恶龙')
input('传闻中,恶龙无恶不作,不仅袭击村镇和路过的商队,还抢走了王国的公主')
input('国王为了王国的安宁,许诺凡诛杀恶龙者,便将公主许配给他')
input('你应召踏上了拯救公主的旅程..')

Game()