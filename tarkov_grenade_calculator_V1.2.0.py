import math,webbrowser,tkinter as tk
from tkinter import ttk,messagebox
APP_NAME="Tarkov Grenade Calculator";AUTHOR_NAME="Mr.J.And";GITHUB_REPOSITORY="Mr-J-And114/Tarkov-Grenade-Calculator";MAP_URL="https://tarkov.dev/maps/"
G=9.81;DT=0.006;MAXT=25.0
AMMO={"AGS-30":(185.0,0.316,0.000135),"VOG-25":(76.0,0.204,0.000160),"40×46mm":(76.0,0.204,0.000160),"Custom":(185.0,0.316,0.000135)}
ZH={"window_title":"塔科夫榴弹射击辅助","language":"语言","ammo_preset":"弹药预设","current_ammo":"当前弹药","current_velocity":"当前初速","bc":"弹道系数 BC","drag_k":"阻力系数 K","set_velocity":"设置参数","restore_default":"恢复 AGS","manual":"说明书","open_map":"打开地图","tab_mode1":"模式1：距离与高低差","tab_mode2":"模式2：坐标计算","tab_mode3":"模式3：动态射表","tab_mode4":"模式4：角度/密位测高","input":"输入","result":"结果","calculate":"计算","generate":"生成射表","distance":"水平距离","horizontal_distance":"水平距离 m","height_difference":"高低差 m","mode1_title":"根据水平距离和高低差，使用 初速 + BC + K 阻力模型计算俯仰角。","height_rule_short":"高低差 = 目标高度 - 炮位高度；正数表示目标更高，负数表示目标更低。","mode2_title":"根据炮位和目标坐标计算距离、方位角与阻力弹道俯仰角。","launcher_x":"炮位 X","launcher_y":"炮位 Y","launcher_z":"炮位高度 Z","target_x":"目标 X","target_y":"目标 Y","target_z":"目标高度 Z","real_direction":"目标相对炮位的真实方位","azimuth_rule":"方位角：北=0°，东=90°，南=180°，西=270°","mode3_title":"根据当前弹药的初速、BC、K 动态生成弹道射表。若存在高低差，请使用模式1或模式2。","step":"步进 m","table_header":"动态阻力弹道射表","same_height_condition":"条件：目标和炮位处于同一水平面，高低差 = 0。","range":"距离","low_arc":"低弹道角","high_arc":"高弹道角","velocity":"速度","tof":"飞行时间","drop":"水平射击下坠","mode4_title":"根据角度或瞄准镜密位估算目标相对观测点的高度差。","m4_hint":"角度向上为正，向下为负；直线距离用 sin，水平距离用 tan。","range_value":"距离 m","angle_value":"角度/密位值","angle_unit":"角度单位","distance_type":"距离类型","sight_height":"瞄准镜离地高度 m","deg":"度","mil":"密位/mrad","slant":"直线距离/斜距","horizontal":"水平距离","height_from_optic":"目标相对瞄准镜高度差","height_from_ground":"目标相对观测点地面高度","calc_horizontal":"换算水平距离","calc_slant":"换算直线距离","north":"北","north_east":"东北","east":"东","south_east":"东南","south":"南","south_west":"西南","west":"西","north_west":"西北","input_error":"输入错误","must_number":"必须输入数字。","must_positive":"必须大于 0。","success":"设置成功","restored":"已恢复默认 AGS","impossible":"无法命中","possible_reason":"可能原因：距离过远、目标过高，或当前初速/BC/K 参数不适合。","azimuth":"方位角","raw_delta":"原始坐标差","corrected_east":"修正后东向分量","corrected_north":"修正后北向分量","ballistic_window_title":"设置弹道参数","new_velocity":"炮弹初速 m/s","new_bc":"Ballistic Coefficient","new_k":"阻力系数 K","temporary_velocity_hint":"该设置会切换为 Custom，仅在本次运行期间有效，关闭软件后不会保存。","apply":"应用","manual_title":"说明书"}
EN={"window_title":"Tarkov Grenade Calculator","language":"Language","ammo_preset":"Ammo Preset","current_ammo":"Current Ammo","current_velocity":"Current Velocity","bc":"Ballistic Coefficient","drag_k":"Drag K","set_velocity":"Set Params","restore_default":"Restore AGS","manual":"Manual","open_map":"Open Map","tab_mode1":"Mode 1: Distance + Height","tab_mode2":"Mode 2: Coordinates","tab_mode3":"Mode 3: Dynamic Table","tab_mode4":"Mode 4: Angle/Mil Height","input":"Input","result":"Result","calculate":"Calculate","generate":"Generate Table","distance":"Horizontal Distance","horizontal_distance":"Horizontal Distance m","height_difference":"Height Difference m","mode1_title":"Calculate elevation using muzzle velocity, BC and drag K.","height_rule_short":"Height difference = target height - launcher height. Positive means higher, negative means lower.","mode2_title":"Calculate distance, azimuth and drag-model elevation by coordinates.","launcher_x":"Launcher X","launcher_y":"Launcher Y","launcher_z":"Launcher Height Z","target_x":"Target X","target_y":"Target Y","target_z":"Target Height Z","real_direction":"Real direction of target relative to launcher","azimuth_rule":"Azimuth: North=0°, East=90°, South=180°, West=270°","mode3_title":"Generate a dynamic ballistic table from current muzzle velocity, BC and drag K.","step":"Step m","table_header":"Dynamic Drag Ballistic Table","same_height_condition":"Condition: target and launcher are at same height, height difference = 0.","range":"Range","low_arc":"Low Arc","high_arc":"High Arc","velocity":"Velocity","tof":"Time","drop":"Zero-Angle Drop","mode4_title":"Estimate target height difference by angle or scope mil/mrad.","m4_hint":"Positive angle means upward, negative means downward. Use sin for slant range, tan for horizontal range.","range_value":"Distance m","angle_value":"Angle/Mil Value","angle_unit":"Angle Unit","distance_type":"Distance Type","sight_height":"Sight Height Above Ground m","deg":"Degree","mil":"Mil/mrad","slant":"Slant Range","horizontal":"Horizontal Range","height_from_optic":"Height Difference From Optic","height_from_ground":"Target Height From Observer Ground","calc_horizontal":"Converted Horizontal Range","calc_slant":"Converted Slant Range","north":"North","north_east":"North-East","east":"East","south_east":"South-East","south":"South","south_west":"South-West","west":"West","north_west":"North-West","input_error":"Input Error","must_number":"must be a number.","must_positive":"must be greater than 0.","success":"Success","restored":"Default AGS Restored","impossible":"Impossible","possible_reason":"Possible reason: too far, too high, or unsuitable velocity/BC/K.","azimuth":"Azimuth","raw_delta":"Raw Coordinate Delta","corrected_east":"Corrected East Component","corrected_north":"Corrected North Component","ballistic_window_title":"Set Ballistic Parameters","new_velocity":"Projectile Velocity m/s","new_bc":"Ballistic Coefficient","new_k":"Drag K","temporary_velocity_hint":"This switches ammo to Custom and is temporary. It will not be saved after closing.","apply":"Apply","manual_title":"Manual"}
LANG={"zh":ZH,"en":EN}
DK=["north","north_east","east","south_east","south","south_west","west","north_west"]
DS={"north":(0,1),"north_east":(1,1),"east":(1,0),"south_east":(1,-1),"south":(0,-1),"south_west":(-1,-1),"west":(-1,0),"north_west":(-1,1)}
def fnum(s,n,l):
    try:return float(s.strip())
    except Exception:raise ValueError(f"{n} {LANG[l]['must_number']}")
def istep(s):return int(float(s.strip()))
def az(e,n):a=math.degrees(math.atan2(e,n));return a+360 if a<0 else a
def hba(r,a,u,t):
    q=math.radians(a) if u=="deg" else a/1000
    if t=="slant":return r*math.sin(q),r*math.cos(q),r,q
    c=math.cos(q);return r*math.tan(q),r,None if abs(c)<1e-12 else r/c,q
def vt(x,v,b,k):return v*math.exp(-(k/b)*x)
def tof(x,v,b,k):
    l=k/b
    return x/v if abs(l)<1e-12 else (math.exp(l*x)-1)/(l*v)
def drop(x,v,b,k):t=tof(x,v,b,k);return -0.5*G*t*t*100
def sim(a,tx,v,b,k):
    if tx<=0 or v<=0 or b<=0 or k<0:return None
    r=math.radians(a);x=y=t=0.0;vx=v*math.cos(r);vy=v*math.sin(r);l=k/b;lx=ly=lt=0.0;lvx=vx;lvy=vy;hp=math.hypot
    while t<MAXT:
        s=hp(vx,vy);vx+=-l*s*vx*DT;vy+=(-G-l*s*vy)*DT;x+=vx*DT;y+=vy*DT;t+=DT
        if x>=tx:
            q=0 if abs(x-lx)<1e-12 else (tx-lx)/(x-lx);ivx=lvx+(vx-lvx)*q;ivy=lvy+(vy-lvy)*q
            return ly+(y-ly)*q,lt+(t-lt)*q,hp(ivx,ivy)
        if x<lx and t>.5 or y<-5000:break
        lx,ly,lt,lvx,lvy=x,y,t,vx,vy
    return None
def err(a,d,h,v,b,k):
    r=sim(a,d,v,b,k);return None if r is None else r[0]-h
def solve(d,h,v,b,k):
    if d<=0 or v<=0 or b<=0:return []
    roots=[];last=None
    a=-45.0
    while a<=85.0001:
        e=err(a,d,h,v,b,k)
        if e is not None and math.isfinite(e):
            if last:
                a1,e1=last
                if abs(e1)<1e-4:roots.append(a1)
                elif e1*e<=0:
                    lo,hi,elo=a1,a,e1
                    for _ in range(24):
                        m=(lo+hi)/2;em=err(m,d,h,v,b,k)
                        if em is None:break
                        if abs(em)<1e-5:lo=hi=m;break
                        if elo*em<=0:hi=m
                        else:lo=m;elo=em
                    r=(lo+hi)/2
                    if all(abs(r-x)>.05 for x in roots):roots.append(r)
                    if len(roots)>=2:break
            last=(a,e)
        a+=0.5
    return roots[:2]
class App:
    def __init__(s,root):
        s.root=root;s.lang="zh";s.ammo="AGS-30";s.v,s.bc,s.k=AMMO[s.ammo];s.cache={}
        for n,val in [("m1d","300"),("m1h","0"),("m2x1","0"),("m2y1","0"),("m2z1","0"),("m2x2","300"),("m2y2","0"),("m2z2","0"),("m3step","25"),("m4r","800"),("m4a","15"),("m4sight","0")]:setattr(s,n,tk.StringVar(value=val))
        s.m2dir="east";s.m4unit="mil";s.m4type="slant";root.geometry("1180x780");root.minsize(1060,700);s.build()
    def t(s,k):return LANG[s.lang][k]
    def roots(s,d,h):
        key=(round(d,3),round(h,3),round(s.v,6),round(s.bc,9),round(s.k,12))
        if key not in s.cache:s.cache[key]=solve(d,h,s.v,s.bc,s.k)
        return s.cache[key]
    def build(s):
        for c in s.root.winfo_children():c.destroy()
        s.root.title(f"{APP_NAME} - {s.t('window_title')}");s.top();s.tabs();s.status()
    def top(s):
        f=ttk.Frame(s.root);f.pack(fill=tk.X,padx=10,pady=(8,4));f.columnconfigure(0,weight=1);s.stat=ttk.Label(f,anchor="w");s.stat.grid(row=0,column=0,sticky="ew",padx=(0,6))
        ttk.Label(f,text=s.t("ammo_preset")).grid(row=0,column=1,padx=3);s.ammov=tk.StringVar(value=s.ammo);cb=ttk.Combobox(f,textvariable=s.ammov,values=list(AMMO),state="readonly",width=10);cb.grid(row=0,column=2,padx=3);cb.bind("<<ComboboxSelected>>",s.ammo_chg)
        ttk.Label(f,text=s.t("language")).grid(row=0,column=3,padx=3);s.langv=tk.StringVar(value="中文" if s.lang=="zh" else "English");lc=ttk.Combobox(f,textvariable=s.langv,values=["中文","English"],state="readonly",width=8);lc.grid(row=0,column=4,padx=3);lc.bind("<<ComboboxSelected>>",lambda e:(setattr(s,"lang","zh" if s.langv.get()=="中文" else "en"),s.build()))
        for i,(txt,cmd) in enumerate([(s.t("set_velocity"),s.open_ballistic),(s.t("restore_default"),s.restore),(s.t("manual"),s.manual),(s.t("open_map"),lambda:webbrowser.open(MAP_URL))],5):ttk.Button(f,text=txt,command=cmd,width=10).grid(row=0,column=i,padx=2)
    def status(s):s.stat.config(text=f"{s.t('current_ammo')}: {s.ammo}    {s.t('current_velocity')}: {s.v:.3f} m/s    {s.t('bc')}: {s.bc:.3f}    {s.t('drag_k')}: {s.k:.6f}")
    def ammo_chg(s,e=None):
        s.ammo=s.ammov.get();s.v,s.bc,s.k=AMMO[s.ammo];s.cache.clear();s.status()
        if hasattr(s,"r3"):s.table()
    def tabs(s):
        s.nb=ttk.Notebook(s.root);s.nb.pack(fill=tk.BOTH,expand=True,padx=10,pady=(4,10));s.tab1=ttk.Frame(s.nb);s.tab2=ttk.Frame(s.nb);s.tab3=ttk.Frame(s.nb);s.tab4=ttk.Frame(s.nb)
        for tab,k in [(s.tab1,"tab_mode1"),(s.tab2,"tab_mode2"),(s.tab3,"tab_mode3"),(s.tab4,"tab_mode4")]:s.nb.add(tab,text=s.t(k))
        s.mode1();s.mode2();s.mode3();s.mode4()
    def ent(s,p,lab,var,r,c,w=14):ttk.Label(p,text=lab).grid(row=r,column=c,sticky="e",padx=8,pady=8);ttk.Entry(p,textvariable=var,width=w).grid(row=r,column=c+1,sticky="w",padx=8,pady=8)
    def text(s,p):
        lf=ttk.LabelFrame(p,text=s.t("result"));lf.grid(row=2,column=0,sticky="nsew",padx=14,pady=8);lf.rowconfigure(0,weight=1);lf.columnconfigure(0,weight=1);tx=tk.Text(lf,wrap=tk.WORD,height=12);tx.grid(row=0,column=0,sticky="nsew",padx=(8,0),pady=8);sb=ttk.Scrollbar(lf,orient=tk.VERTICAL,command=tx.yview);sb.grid(row=0,column=1,sticky="ns",padx=(0,8),pady=8);tx.configure(yscrollcommand=sb.set);return tx
    def mode1(s):
        f=s.tab1;f.columnconfigure(0,weight=1);f.rowconfigure(2,weight=1);ttk.Label(f,text=f"{s.t('mode1_title')}\n{s.t('height_rule_short')}",justify=tk.LEFT,wraplength=1080).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=s.t("input"));inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8);inp.columnconfigure(5,weight=1);s.ent(inp,s.t("horizontal_distance"),s.m1d,0,0,16);s.ent(inp,s.t("height_difference"),s.m1h,0,2,16);ttk.Button(inp,text=s.t("calculate"),command=s.calc1,width=14).grid(row=0,column=4,sticky="w",padx=8,pady=10);s.r1=s.text(f)
    def calc1(s):
        try:d=fnum(s.m1d.get(),s.t("horizontal_distance"),s.lang);h=fnum(s.m1h.get(),s.t("height_difference"),s.lang)
        except ValueError as e:return messagebox.showerror(s.t("input_error"),str(e))
        r=s.roots(d,h);L=[f"{s.t('current_ammo')}: {s.ammo}",f"{s.t('current_velocity')}: {s.v:.3f} m/s",f"{s.t('bc')}: {s.bc:.3f}",f"{s.t('drag_k')}: {s.k:.6f}",f"{s.t('distance')}: {d:.3f} m",f"{s.t('height_difference')}: {h:.3f} m","",s.t("height_rule_short"),""]
        if not r:L+=[f"{s.t('low_arc')}: {s.t('impossible')}",s.t("possible_reason")]
        else:
            L+=[f"{s.t('low_arc')}: {r[0]:.3f}°",f"{s.t('high_arc')}: {r[1]:.3f}°" if len(r)>1 else f"{s.t('high_arc')}: {s.t('impossible')}"];q=sim(r[0],d,s.v,s.bc,s.k)
            if q:L+=["",f"{s.t('velocity')}: {q[2]:.3f} m/s",f"{s.t('tof')}: {q[1]:.3f} s"]
        s.set_text(s.r1,"\n".join(L))
    def mode2(s):
        f=s.tab2;f.columnconfigure(0,weight=1);f.rowconfigure(2,weight=1);ttk.Label(f,text=f"{s.t('mode2_title')}\n{s.t('height_rule_short')}\n{s.t('azimuth_rule')}",justify=tk.LEFT,wraplength=1080).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=s.t("input"));inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8)
        for i in range(6):inp.columnconfigure(i,weight=1)
        for lab,var,r,c in [(s.t("launcher_x"),s.m2x1,0,0),(s.t("launcher_y"),s.m2y1,0,2),(s.t("launcher_z"),s.m2z1,0,4),(s.t("target_x"),s.m2x2,1,0),(s.t("target_y"),s.m2y2,1,2),(s.t("target_z"),s.m2z2,1,4)]:s.ent(inp,lab,var,r,c)
        ttk.Label(inp,text=s.t("real_direction")).grid(row=2,column=0,sticky="e",padx=8,pady=10);s.dirv=tk.StringVar(value=s.t(s.m2dir));cb=ttk.Combobox(inp,textvariable=s.dirv,values=[s.t(k) for k in DK],state="readonly",width=18);cb.grid(row=2,column=1,sticky="w",padx=8,pady=10);cb.bind("<<ComboboxSelected>>",s.dir_chg);ttk.Button(inp,text=s.t("calculate"),command=s.calc2,width=14).grid(row=2,column=4,sticky="e",padx=8,pady=10);s.r2=s.text(f)
    def dir_chg(s,e=None):
        for k in DK:
            if s.t(k)==s.dirv.get():s.m2dir=k;break
    def calc2(s):
        try:x1,y1,z1,x2,y2,z2=[fnum(v.get(),n,s.lang) for v,n in [(s.m2x1,s.t("launcher_x")),(s.m2y1,s.t("launcher_y")),(s.m2z1,s.t("launcher_z")),(s.m2x2,s.t("target_x")),(s.m2y2,s.t("target_y")),(s.m2z2,s.t("target_z"))]]
        except ValueError as e:return messagebox.showerror(s.t("input_error"),str(e))
        dx=x2-x1;dy=y2-y1;d=math.hypot(dx,dy);h=z2-z1;se,sn=DS[s.m2dir];east=se*abs(dx) if se else 0.0;north=sn*abs(dy) if sn else 0.0;A=az(east,north);r=s.roots(d,h)
        L=[f"{s.t('current_ammo')}: {s.ammo}",f"{s.t('current_velocity')}: {s.v:.3f} m/s",f"{s.t('bc')}: {s.bc:.3f}",f"{s.t('drag_k')}: {s.k:.6f}","",f"{s.t('launcher_x')}, {s.t('launcher_y')}, {s.t('launcher_z')}: ({x1:.3f}, {y1:.3f}, {z1:.3f})",f"{s.t('target_x')}, {s.t('target_y')}, {s.t('target_z')}: ({x2:.3f}, {y2:.3f}, {z2:.3f})","",f"{s.t('raw_delta')}: dx = {dx:.3f}, dy = {dy:.3f}",f"{s.t('distance')}: {d:.3f} m",f"{s.t('height_difference')}: {h:.3f} m","",f"{s.t('real_direction')}: {s.t(s.m2dir)}",f"{s.t('corrected_east')}: {east:.3f} m",f"{s.t('corrected_north')}: {north:.3f} m",f"{s.t('azimuth')}: {A:.3f}°",s.t("azimuth_rule"),""]
        if not r:L+=[f"{s.t('low_arc')}: {s.t('impossible')}",s.t("possible_reason")]
        else:
            L+=[f"{s.t('low_arc')}: {r[0]:.3f}°",f"{s.t('high_arc')}: {r[1]:.3f}°" if len(r)>1 else f"{s.t('high_arc')}: {s.t('impossible')}"];q=sim(r[0],d,s.v,s.bc,s.k)
            if q:L+=["",f"{s.t('velocity')}: {q[2]:.3f} m/s",f"{s.t('tof')}: {q[1]:.3f} s"]
        s.set_text(s.r2,"\n".join(L))
    def mode3(s):
        f=s.tab3;f.columnconfigure(0,weight=1);f.rowconfigure(2,weight=1);ttk.Label(f,text=s.t("mode3_title"),justify=tk.LEFT,wraplength=1080).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=s.t("input"));inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8);inp.columnconfigure(3,weight=1);s.ent(inp,s.t("step"),s.m3step,0,0);ttk.Button(inp,text=s.t("generate"),command=s.table,width=14).grid(row=0,column=2,sticky="w",padx=8,pady=10)
        lf=ttk.LabelFrame(f,text=s.t("tab_mode3"));lf.grid(row=2,column=0,sticky="nsew",padx=14,pady=8);lf.rowconfigure(0,weight=1);lf.columnconfigure(0,weight=1);s.r3=tk.Text(lf,wrap=tk.NONE);s.r3.grid(row=0,column=0,sticky="nsew",padx=(8,0),pady=8);sy=ttk.Scrollbar(lf,orient=tk.VERTICAL,command=s.r3.yview);sx=ttk.Scrollbar(lf,orient=tk.HORIZONTAL,command=s.r3.xview);sy.grid(row=0,column=1,sticky="ns",padx=(0,8),pady=8);sx.grid(row=1,column=0,sticky="ew",padx=(8,0),pady=(0,8));s.r3.configure(yscrollcommand=sy.set,xscrollcommand=sx.set);s.table()
    def table(s):
        try:st=istep(s.m3step.get())
        except Exception:return messagebox.showerror(s.t("input_error"),f"{s.t('step')} {s.t('must_number')}")
        if st<=0:return messagebox.showerror(s.t("input_error"),f"{s.t('step')} {s.t('must_positive')}")
        L=[f"{s.t('table_header')} - {s.ammo}",f"{s.t('current_velocity')}: {s.v:.3f} m/s    {s.t('bc')}: {s.bc:.3f}    {s.t('drag_k')}: {s.k:.6f}",s.t("same_height_condition"),"",f"{s.t('range'):>8} | {s.t('low_arc'):>12} | {s.t('high_arc'):>12} | {s.t('velocity'):>12} | {s.t('tof'):>10} | {s.t('drop'):>16}","-"*86]
        for d in range(0,1001,st):
            if d==0:lo,hi,vv,tt,dd="0.000°","-",s.v,0.0,-0.0
            else:
                r=s.roots(float(d),0.0);lo=s.t("impossible") if not r else f"{r[0]:.3f}°";hi=s.t("impossible") if len(r)<2 else f"{r[1]:.3f}°";vv=vt(d,s.v,s.bc,s.k);tt=tof(d,s.v,s.bc,s.k);dd=-0.5*G*tt*tt*100
            L.append(f"{d:8d} | {lo:>12} | {hi:>12} | {vv:12.2f} | {tt:10.2f} | {dd:16.2f}")
        s.set_text(s.r3,"\n".join(L))
    def mode4(s):
        f=s.tab4;f.columnconfigure(0,weight=1);f.rowconfigure(2,weight=1);ttk.Label(f,text=f"{s.t('mode4_title')}\n{s.t('m4_hint')}",justify=tk.LEFT,wraplength=1080).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=s.t("input"));inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8)
        for i in range(8):inp.columnconfigure(i,weight=1)
        s.ent(inp,s.t("range_value"),s.m4r,0,0,14);s.ent(inp,s.t("angle_value"),s.m4a,0,2,14);s.ent(inp,s.t("sight_height"),s.m4sight,0,4,14)
        ttk.Label(inp,text=s.t("angle_unit")).grid(row=1,column=0,sticky="e",padx=8,pady=8);s.m4unitv=tk.StringVar(value=s.t(s.m4unit));c1=ttk.Combobox(inp,textvariable=s.m4unitv,values=[s.t("deg"),s.t("mil")],state="readonly",width=16);c1.grid(row=1,column=1,sticky="w",padx=8,pady=8);c1.bind("<<ComboboxSelected>>",lambda e:setattr(s,"m4unit","deg" if s.m4unitv.get()==s.t("deg") else "mil"))
        ttk.Label(inp,text=s.t("distance_type")).grid(row=1,column=2,sticky="e",padx=8,pady=8);s.m4typev=tk.StringVar(value=s.t(s.m4type));c2=ttk.Combobox(inp,textvariable=s.m4typev,values=[s.t("slant"),s.t("horizontal")],state="readonly",width=18);c2.grid(row=1,column=3,sticky="w",padx=8,pady=8);c2.bind("<<ComboboxSelected>>",lambda e:setattr(s,"m4type","slant" if s.m4typev.get()==s.t("slant") else "horizontal"));ttk.Button(inp,text=s.t("calculate"),command=s.calc4,width=14).grid(row=1,column=5,sticky="w",padx=8,pady=8);s.r4=s.text(f)
    def calc4(s):
        try:r=fnum(s.m4r.get(),s.t("range_value"),s.lang);a=fnum(s.m4a.get(),s.t("angle_value"),s.lang);sh=fnum(s.m4sight.get(),s.t("sight_height"),s.lang)
        except ValueError as e:return messagebox.showerror(s.t("input_error"),str(e))
        if r<=0:return messagebox.showerror(s.t("input_error"),f"{s.t('range_value')} {s.t('must_positive')}")
        h,hor,sl,rad=hba(r,a,s.m4unit,s.m4type);s.set_text(s.r4,"\n".join([s.t("mode4_title"),"",f"{s.t('range_value')}: {r:.3f} m",f"{s.t('distance_type')}: {s.t(s.m4type)}",f"{s.t('angle_value')}: {a:.3f} {s.t(s.m4unit)}",f"radian: {rad:.6f}",f"{s.t('sight_height')}: {sh:.3f} m","",f"{s.t('height_from_optic')}: {h:.3f} m",f"{s.t('height_from_ground')}: {h+sh:.3f} m",f"{s.t('calc_horizontal')}: {hor:.3f} m",f"{s.t('calc_slant')}: {'N/A' if sl is None else f'{sl:.3f} m'}","",s.t("m4_hint")]))
    def open_ballistic(s):
        w=tk.Toplevel(s.root);w.title(s.t("ballistic_window_title"));w.geometry("500x290");w.resizable(False,False)
        ttk.Label(w,text=f"{s.t('current_ammo')}: {s.ammo}\n{s.t('current_velocity')}: {s.v:.3f} m/s\n{s.t('bc')}: {s.bc:.3f}\n{s.t('drag_k')}: {s.k:.6f}\n\n{s.t('temporary_velocity_hint')}",justify=tk.LEFT,wraplength=460).pack(anchor="w",padx=16,pady=14)
        f=ttk.Frame(w);f.pack(fill=tk.X,padx=16,pady=8);vv=tk.StringVar(value=f"{s.v:.3f}");bv=tk.StringVar(value=f"{s.bc:.3f}");kv=tk.StringVar(value=f"{s.k:.6f}")
        for i,(lab,var) in enumerate([(s.t("new_velocity"),vv),(s.t("new_bc"),bv),(s.t("new_k"),kv)]):ttk.Label(f,text=lab).grid(row=i,column=0,sticky="e",padx=8,pady=5);ttk.Entry(f,textvariable=var,width=16).grid(row=i,column=1,sticky="w",padx=8,pady=5)
        def ap():
            try:nv=fnum(vv.get(),s.t("new_velocity"),s.lang);nb=fnum(bv.get(),s.t("new_bc"),s.lang);nk=fnum(kv.get(),s.t("new_k"),s.lang)
            except ValueError as e:return messagebox.showerror(s.t("input_error"),str(e),parent=w)
            if nv<=0:return messagebox.showerror(s.t("input_error"),f"{s.t('new_velocity')} {s.t('must_positive')}",parent=w)
            if nb<=0:return messagebox.showerror(s.t("input_error"),f"{s.t('new_bc')} {s.t('must_positive')}",parent=w)
            if nk<0:return messagebox.showerror(s.t("input_error"),f"{s.t('new_k')} {s.t('must_positive')}",parent=w)
            s.ammo="Custom";s.v=nv;s.bc=nb;s.k=nk;AMMO["Custom"]=(nv,nb,nk);s.cache.clear();s.build();messagebox.showinfo(s.t("success"),f"{s.t('current_velocity')}: {nv:.3f} m/s\n{s.t('bc')}: {nb:.3f}\n{s.t('drag_k')}: {nk:.6f}",parent=w);w.destroy()
        ttk.Button(w,text=s.t("apply"),command=ap,width=12).pack(pady=12)
    def restore(s):
        s.ammo="AGS-30";s.v,s.bc,s.k=AMMO[s.ammo];s.cache.clear();s.build();messagebox.showinfo(s.t("restored"),f"{s.t('current_ammo')}: {s.ammo}\n{s.t('current_velocity')}: {s.v:.3f} m/s\n{s.t('bc')}: {s.bc:.3f}\n{s.t('drag_k')}: {s.k:.6f}")
    def manual(s):
        w=tk.Toplevel(s.root);w.title(s.t("manual_title"));w.geometry("820x680");tx=tk.Text(w,wrap=tk.WORD);tx.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=(10,0),pady=10);sb=ttk.Scrollbar(w,orient=tk.VERTICAL,command=tx.yview);sb.pack(side=tk.RIGHT,fill=tk.Y,padx=(0,10),pady=10);tx.configure(yscrollcommand=sb.set);tx.insert(tk.END,s.manual_text());tx.configure(state=tk.DISABLED)
    def manual_text(s):
        return f"""
{APP_NAME}
============================================================
Author / 作者：{AUTHOR_NAME}
GitHub：{GITHUB_REPOSITORY}
Map：{MAP_URL}

本工具只计算弹道相关内容，不计算伤害、穿透或爆炸效果。

内置弹药：
AGS-30：v0=185 m/s, BC=0.316, K=0.000135
VOG-25：v0=76 m/s, BC=0.204, K=0.000160
40×46mm：v0=76 m/s, BC=0.204, K=0.000160
Custom：用户自定义 v0、BC、K。

速度衰减：
v(x)=v0*exp[-(K/BC)*x]

飞行时间：
t(x)=[exp((K/BC)*x)-1]/[(K/BC)*v0]

二维阻力积分：
speed=sqrt(vx²+vy²)
ax=-(K/BC)*speed*vx
ay=-g-(K/BC)*speed*vy

高低差：
高低差 = 目标高度 - 炮位高度。

方位角：
北=0°，东=90°，南=180°，西=270°。

射表：
射表仅显示距离、低弹道角、高弹道角、速度、飞行时间、水平射击下坠。

Custom 参数仅本次运行有效。
"""
    @staticmethod
    def set_text(w,t):w.configure(state=tk.NORMAL);w.delete("1.0",tk.END);w.insert(tk.END,t);w.configure(state=tk.NORMAL)
def main():root=tk.Tk();App(root);root.mainloop()
if __name__=="__main__":main()