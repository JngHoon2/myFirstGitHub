import tkinter as tk

window = tk.Tk()
window.geometry('1200x720+50+50')
window.resizable(False, False)

RunTimelbl = tk.Label(window, text= '반복 실행 횟수 :')
ASurviveTimelbl = tk.Label(window, text= 'A가 살아남은 횟수 :')
BSurviveTimelbl = tk.Label(window, text= 'B가 살아남은 횟수 :')
CSurviveTimelbl = tk.Label(window, text= 'C가 살아남은 횟수 :')
NSurviveTimelbl = tk.Label(window, text= '전부 죽어버린 횟수 :')

RunTimelbl.place(x= 100, y= 50)
ASurviveTimelbl.place(x= 100, y= 100)
BSurviveTimelbl.place(x= 100, y= 150)
CSurviveTimelbl.place(x= 100, y= 200)
NSurviveTimelbl.place(x= 100, y= 250)


# 반복 시행 횟수
RT = 0
# 각 플레이어가 살아남은 횟수
AST = 0
BST = 0
CST = 0
NST = 0

RTlbl = tk.Label(window, text= str(AST))
ASTlbl = tk.Label(window, text= str(AST))
BSTlbl = tk.Label(window, text= str(BST))
CSTlbl = tk.Label(window, text= str(CST))
NSTlbl = tk.Label(window, text= str(CST))

RTlbl.place(x= 210, y= 50)
ASTlbl.place(x= 210, y= 100)
BSTlbl.place(x= 210, y= 150)
CSTlbl.place(x= 210, y= 200)
NSTlbl.place(x= 210, y= 250)


loglbl = tk.Label(window, text= 'Process log')
loglbl.place(x= 100, y= 300)
logBox = tk.Entry(window, width= 40, bg= '#E0E0E0', state= 'readonly')
logBox.place(x= 100, y= 320)


window.mainloop()