import tkinter as tk

window = tk.Tk()
window.geometry('1200x720+50+50')
window.resizable(False, False)

RunTimelbl = tk.Label(window, text= '반복 실행 횟수 :')
ASurviveTimelbl = tk.Label(window, text= 'A가 살아남은 횟수 :')
BSurviveTimelbl = tk.Label(window, text= 'B가 살아남은 횟수 :')
CSurviveTimelbl = tk.Label(window, text= 'C가 살아남은 횟수 :')
NSurviveTimelbl = tk.Label(window, text= '전부 죽어버린 횟수 :')

RunTimelbl.place(x= 100, y= 400)
ASurviveTimelbl.place(x= 100, y= 450)
BSurviveTimelbl.place(x= 100, y= 500)
CSurviveTimelbl.place(x= 100, y= 550)
NSurviveTimelbl.place(x= 100, y= 600)


# 반복 시행 횟수
RT = 0
# 각 플레이어가 살아남은 횟수
AST = 0
BST = 0
CST = 0
NST = 0

RTlbl = tk.Label(window, text= str(RT))
ASTlbl = tk.Label(window, text= str(AST))
BSTlbl = tk.Label(window, text= str(BST))
CSTlbl = tk.Label(window, text= str(CST))
NSTlbl = tk.Label(window, text= str(NST))

RTlbl.place(x= 210, y= 400)
ASTlbl.place(x= 210, y= 450)
BSTlbl.place(x= 210, y= 500)
CSTlbl.place(x= 210, y= 550)
NSTlbl.place(x= 210, y= 600)


loglbl = tk.Label(window, text= 'Process log')
loglbl.place(x= 240, y= 50)
logBox = tk.Entry(window, width= 40, bg= '#E0E0E0', state= 'readonly')
logBox.place(x= 100, y= 70)


window.mainloop()