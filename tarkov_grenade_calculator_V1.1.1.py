import math, webbrowser, tkinter as tk
from tkinter import ttk, messagebox

APP_NAME="Tarkov Grenade Calculator"; AUTHOR_NAME="Mr.J.And"; GITHUB_REPOSITORY="Mr-J-And114/Tarkov-Grenade-Calculator"; MAP_URL="https://tarkov.dev/maps/"
G=9.81; DEFAULT_CALIBRATION_DISTANCE=300.0; DEFAULT_CALIBRATION_ANGLE_DEG=2.5
DEFAULT_VELOCITY=math.sqrt(DEFAULT_CALIBRATION_DISTANCE*G/math.sin(math.radians(DEFAULT_CALIBRATION_ANGLE_DEG*2)))

LANG={
"zh":{
"window_title":"塔科夫榴弹射击辅助","language":"语言","current_velocity":"当前初速","default_ags":"默认 AGS","calibration":"校准点","set_velocity":"设置初速","restore_default":"恢复默认","manual":"说明书","open_map":"打开地图",
"tab_mode1":"模式1：距离与高低差","tab_mode2":"模式2：坐标计算","tab_mode3":"模式3：射表","tab_mode4":"模式4：角度/密位测高",
"input":"输入","result":"结果","calculate":"计算","generate":"生成射表","distance":"水平距离","horizontal_distance":"水平距离 m","height_difference":"高低差 m",
"mode1_title":"根据水平距离和高低差计算俯仰角。","height_rule_short":"高低差 = 目标高度 - 炮位高度；正数表示目标更高，负数表示目标更低。",
"mode2_title":"根据炮位和目标坐标计算距离、方位角与俯仰角。","launcher_x":"炮位 X","launcher_y":"炮位 Y","launcher_z":"炮位高度 Z","target_x":"目标 X","target_y":"目标 Y","target_z":"目标高度 Z","real_direction":"目标相对炮位的真实方位","azimuth_rule":"方位角：北=0°，东=90°，南=180°，西=270°",
"mode3_title":"生成 0~1000 米水平面射表。若存在高低差，请使用模式1或模式2。","step":"步进 m",
"mode4_title":"根据角度或瞄准镜密位估算目标相对观测点的高度差。","m4_hint":"角度向上为正，向下为负；直线距离用 sin，水平距离用 tan。","range_value":"距离 m","angle_value":"角度/密位值","angle_unit":"角度单位","distance_type":"距离类型","sight_height":"瞄准镜离地高度 m","deg":"度","mil":"密位/mrad","slant":"直线距离/斜距","horizontal":"水平距离","height_from_optic":"目标相对瞄准镜高度差","height_from_ground":"目标相对观测点地面高度","calc_horizontal":"换算水平距离","calc_slant":"换算直线距离",
"north":"北","north_east":"东北","east":"东","south_east":"东南","south":"南","south_west":"西南","west":"西","north_west":"西北",
"input_error":"输入错误","must_number":"必须输入数字。","must_positive":"必须大于 0。","success":"设置成功","restored":"已恢复默认",
"low_arc":"低弹道俯仰角","high_arc":"高弹道参考角","impossible":"无法命中","possible_reason":"可能原因：距离过远、目标过高，或当前初速过低。","azimuth":"方位角","raw_delta":"原始坐标差","corrected_east":"修正后东向分量","corrected_north":"修正后北向分量",
"velocity_window_title":"设置炮弹初速","new_velocity":"新的炮弹初速 m/s","temporary_velocity_hint":"该设置仅在本次运行期间有效，关闭软件后不会保存。","apply":"应用",
"table_header":"AGS 水平面射表","same_height_condition":"条件：目标和炮位处于同一水平面，高低差 = 0。","manual_title":"说明书"},
"en":{
"window_title":"Tarkov Grenade Calculator","language":"Language","current_velocity":"Current Velocity","default_ags":"Default AGS","calibration":"Calibration","set_velocity":"Set Velocity","restore_default":"Restore","manual":"Manual","open_map":"Open Map",
"tab_mode1":"Mode 1: Distance + Height","tab_mode2":"Mode 2: Coordinates","tab_mode3":"Mode 3: Firing Table","tab_mode4":"Mode 4: Angle/Mil Height",
"input":"Input","result":"Result","calculate":"Calculate","generate":"Generate Table","distance":"Horizontal Distance","horizontal_distance":"Horizontal Distance m","height_difference":"Height Difference m",
"mode1_title":"Calculate elevation by horizontal distance and height difference.","height_rule_short":"Height difference = target height - launcher height. Positive means higher, negative means lower.",
"mode2_title":"Calculate distance, azimuth and elevation by launcher and target coordinates.","launcher_x":"Launcher X","launcher_y":"Launcher Y","launcher_z":"Launcher Height Z","target_x":"Target X","target_y":"Target Y","target_z":"Target Height Z","real_direction":"Real direction of target relative to launcher","azimuth_rule":"Azimuth: North=0°, East=90°, South=180°, West=270°",
"mode3_title":"Generate a 0-1000m horizontal firing table. Use Mode 1 or Mode 2 if height difference exists.","step":"Step m",
"mode4_title":"Estimate target height difference by angle or scope mil/mrad.","m4_hint":"Positive angle means upward, negative means downward. Use sin for slant range, tan for horizontal range.","range_value":"Distance m","angle_value":"Angle/Mil Value","angle_unit":"Angle Unit","distance_type":"Distance Type","sight_height":"Sight Height Above Ground m","deg":"Degree","mil":"Mil/mrad","slant":"Slant Range","horizontal":"Horizontal Range","height_from_optic":"Height Difference From Optic","height_from_ground":"Target Height From Observer Ground","calc_horizontal":"Converted Horizontal Range","calc_slant":"Converted Slant Range",
"north":"North","north_east":"North-East","east":"East","south_east":"South-East","south":"South","south_west":"South-West","west":"West","north_west":"North-West",
"input_error":"Input Error","must_number":"must be a number.","must_positive":"must be greater than 0.","success":"Success","restored":"Restored",
"low_arc":"Low-arc Elevation","high_arc":"High-arc Reference","impossible":"Impossible","possible_reason":"Possible reason: too far, target too high, or velocity too low.","azimuth":"Azimuth","raw_delta":"Raw Coordinate Delta","corrected_east":"Corrected East Component","corrected_north":"Corrected North Component",
"velocity_window_title":"Set Projectile Velocity","new_velocity":"New Projectile Velocity m/s","temporary_velocity_hint":"This setting is temporary and will not be saved after closing the software.","apply":"Apply",
"table_header":"AGS Horizontal Firing Table","same_height_condition":"Condition: target and launcher are at the same height, height difference = 0.","manual_title":"Manual"}}

DIRECTION_KEYS=["north","north_east","east","south_east","south","south_west","west","north_west"]
DIRECTION_SIGNS={"north":(0,1),"north_east":(1,1),"east":(1,0),"south_east":(1,-1),"south":(0,-1),"south_west":(-1,-1),"west":(-1,0),"north_west":(-1,1)}

def low_ang(x,h,v):
    if x<=0 or v<=0:return None
    d=v**4-G*(G*x*x+2*h*v*v)
    if d<0:return None
    return math.degrees(math.atan((v*v-math.sqrt(d))/(G*x)))
def high_ang(x,h,v):
    if x<=0 or v<=0:return None
    d=v**4-G*(G*x*x+2*h*v*v)
    if d<0:return None
    return math.degrees(math.atan((v*v+math.sqrt(d))/(G*x)))
def dist2(x1,y1,x2,y2): return math.hypot(x2-x1,y2-y1)
def azimuth(e,n):
    a=math.degrees(math.atan2(e,n)); return a+360 if a<0 else a
def fnum(s,name,lang):
    try:return float(s.strip())
    except Exception:raise ValueError(f"{name} {LANG[lang]['must_number']}")
def i_step(s):
    return int(float(s.strip()))
def fmt(a): return f"{a:.3f}°"
def height_by_angle(r,a,unit,typ):
    rad=math.radians(a) if unit=="deg" else a/1000.0
    if typ=="slant":
        h=r*math.sin(rad); hor=r*math.cos(rad); sl=r
    else:
        h=r*math.tan(rad); hor=r; c=math.cos(rad); sl=None if abs(c)<1e-12 else r/c
    return h,hor,sl,rad

class App:
    def __init__(self,root):
        self.root=root; self.lang="zh"; self.current_velocity=DEFAULT_VELOCITY
        self.m1d=tk.StringVar(value="300"); self.m1h=tk.StringVar(value="0")
        self.m2x1=tk.StringVar(value="0"); self.m2y1=tk.StringVar(value="0"); self.m2z1=tk.StringVar(value="0"); self.m2x2=tk.StringVar(value="300"); self.m2y2=tk.StringVar(value="0"); self.m2z2=tk.StringVar(value="0"); self.m2dir="east"
        self.m3step=tk.StringVar(value="50")
        self.m4r=tk.StringVar(value="800"); self.m4a=tk.StringVar(value="15"); self.m4sight=tk.StringVar(value="0"); self.m4unit="mil"; self.m4type="slant"
        root.geometry("1080x740"); root.minsize(980,660); self.build()
    def t(self,k): return LANG[self.lang][k]
    def build(self):
        for c in self.root.winfo_children(): c.destroy()
        self.root.title(f"{APP_NAME} - {self.t('window_title')}"); self.top(); self.tabs(); self.update_vel()
    def top(self):
        f=ttk.Frame(self.root); f.pack(fill=tk.X,padx=10,pady=(8,4)); f.columnconfigure(0,weight=1)
        self.vel_lab=ttk.Label(f,anchor="w"); self.vel_lab.grid(row=0,column=0,sticky="ew",padx=(0,8))
        ttk.Label(f,text=self.t("language")).grid(row=0,column=1,padx=4)
        self.langv=tk.StringVar(value="中文" if self.lang=="zh" else "English")
        cb=ttk.Combobox(f,textvariable=self.langv,values=["中文","English"],state="readonly",width=9); cb.grid(row=0,column=2,padx=3); cb.bind("<<ComboboxSelected>>",self.lang_changed)
        for i,(txt,cmd) in enumerate([(self.t("set_velocity"),self.open_vel),(self.t("restore_default"),self.restore),(self.t("manual"),self.manual),(self.t("open_map"),lambda:webbrowser.open(MAP_URL))],3):
            ttk.Button(f,text=txt,command=cmd,width=10).grid(row=0,column=i,padx=3)
    def lang_changed(self,e=None): self.lang="zh" if self.langv.get()=="中文" else "en"; self.build()
    def update_vel(self):
        self.vel_lab.config(text=f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s    {self.t('default_ags')}: {DEFAULT_VELOCITY:.3f} m/s    {self.t('calibration')}: 300m = 2.5°")
    def tabs(self):
        self.nb=ttk.Notebook(self.root); self.nb.pack(fill=tk.BOTH,expand=True,padx=10,pady=(4,10))
        self.tab1=ttk.Frame(self.nb); self.tab2=ttk.Frame(self.nb); self.tab3=ttk.Frame(self.nb); self.tab4=ttk.Frame(self.nb)
        for tab,key in [(self.tab1,"tab_mode1"),(self.tab2,"tab_mode2"),(self.tab3,"tab_mode3"),(self.tab4,"tab_mode4")]: self.nb.add(tab,text=self.t(key))
        self.mode1(); self.mode2(); self.mode3(); self.mode4()
    def text_result(self,parent):
        lf=ttk.LabelFrame(parent,text=self.t("result")); lf.grid(row=2,column=0,sticky="nsew",padx=14,pady=8); lf.rowconfigure(0,weight=1); lf.columnconfigure(0,weight=1)
        tx=tk.Text(lf,wrap=tk.WORD,height=12); tx.grid(row=0,column=0,sticky="nsew",padx=(8,0),pady=8)
        sb=ttk.Scrollbar(lf,orient=tk.VERTICAL,command=tx.yview); sb.grid(row=0,column=1,sticky="ns",padx=(0,8),pady=8); tx.configure(yscrollcommand=sb.set); return tx
    def labent(self,p,lab,var,r,c,w=14):
        ttk.Label(p,text=lab).grid(row=r,column=c,sticky="e",padx=8,pady=8); ttk.Entry(p,textvariable=var,width=w).grid(row=r,column=c+1,sticky="w",padx=8,pady=8)
    def mode1(self):
        f=self.tab1; f.columnconfigure(0,weight=1); f.rowconfigure(2,weight=1)
        ttk.Label(f,text=f"{self.t('mode1_title')}\n{self.t('height_rule_short')}",justify=tk.LEFT,wraplength=980).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=self.t("input")); inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8); inp.columnconfigure(5,weight=1)
        self.labent(inp,self.t("horizontal_distance"),self.m1d,0,0,16); self.labent(inp,self.t("height_difference"),self.m1h,0,2,16)
        ttk.Button(inp,text=self.t("calculate"),command=self.calc1,width=14).grid(row=0,column=4,sticky="w",padx=8,pady=10)
        self.r1=self.text_result(f)
    def calc1(self):
        try:d=fnum(self.m1d.get(),self.t("horizontal_distance"),self.lang); h=fnum(self.m1h.get(),self.t("height_difference"),self.lang)
        except ValueError as e: return messagebox.showerror(self.t("input_error"),str(e))
        lo,hi=low_ang(d,h,self.current_velocity),high_ang(d,h,self.current_velocity)
        lines=[f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s",f"{self.t('distance')}: {d:.3f} m",f"{self.t('height_difference')}: {h:.3f} m","",self.t("height_rule_short"),""]
        lines += [f"{self.t('low_arc')}: {self.t('impossible')}",self.t("possible_reason")] if lo is None else [f"{self.t('low_arc')}: {fmt(lo)}"]
        lines += [f"{self.t('high_arc')}: {self.t('impossible')}"] if hi is None else [f"{self.t('high_arc')}: {fmt(hi)}"]
        self.set_text(self.r1,"\n".join(lines))
    def mode2(self):
        f=self.tab2; f.columnconfigure(0,weight=1); f.rowconfigure(2,weight=1)
        ttk.Label(f,text=f"{self.t('mode2_title')}\n{self.t('height_rule_short')}\n{self.t('azimuth_rule')}",justify=tk.LEFT,wraplength=980).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=self.t("input")); inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8)
        for i in range(6): inp.columnconfigure(i,weight=1)
        for lab,var,r,c in [(self.t("launcher_x"),self.m2x1,0,0),(self.t("launcher_y"),self.m2y1,0,2),(self.t("launcher_z"),self.m2z1,0,4),(self.t("target_x"),self.m2x2,1,0),(self.t("target_y"),self.m2y2,1,2),(self.t("target_z"),self.m2z2,1,4)]: self.labent(inp,lab,var,r,c)
        ttk.Label(inp,text=self.t("real_direction")).grid(row=2,column=0,sticky="e",padx=8,pady=10)
        self.dirv=tk.StringVar(value=self.t(self.m2dir)); cb=ttk.Combobox(inp,textvariable=self.dirv,values=[self.t(k) for k in DIRECTION_KEYS],state="readonly",width=18); cb.grid(row=2,column=1,sticky="w",padx=8,pady=10); cb.bind("<<ComboboxSelected>>",self.dir_changed)
        ttk.Button(inp,text=self.t("calculate"),command=self.calc2,width=14).grid(row=2,column=4,sticky="e",padx=8,pady=10)
        self.r2=self.text_result(f)
    def dir_changed(self,e=None):
        s=self.dirv.get()
        for k in DIRECTION_KEYS:
            if self.t(k)==s: self.m2dir=k; break
    def calc2(self):
        try:
            x1,y1,z1,x2,y2,z2=[fnum(v.get(),n,self.lang) for v,n in [(self.m2x1,self.t("launcher_x")),(self.m2y1,self.t("launcher_y")),(self.m2z1,self.t("launcher_z")),(self.m2x2,self.t("target_x")),(self.m2y2,self.t("target_y")),(self.m2z2,self.t("target_z"))]]
        except ValueError as e: return messagebox.showerror(self.t("input_error"),str(e))
        dx,dy=x2-x1,y2-y1; d=dist2(x1,y1,x2,y2); h=z2-z1; se,sn=DIRECTION_SIGNS[self.m2dir]; east=se*abs(dx) if se else 0.0; north=sn*abs(dy) if sn else 0.0; az=azimuth(east,north); lo,hi=low_ang(d,h,self.current_velocity),high_ang(d,h,self.current_velocity)
        lines=[f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s","",f"{self.t('launcher_x')}, {self.t('launcher_y')}, {self.t('launcher_z')}: ({x1:.3f}, {y1:.3f}, {z1:.3f})",f"{self.t('target_x')}, {self.t('target_y')}, {self.t('target_z')}: ({x2:.3f}, {y2:.3f}, {z2:.3f})","",f"{self.t('raw_delta')}: dx = {dx:.3f}, dy = {dy:.3f}",f"{self.t('distance')}: {d:.3f} m",f"{self.t('height_difference')}: {h:.3f} m","",f"{self.t('real_direction')}: {self.t(self.m2dir)}",f"{self.t('corrected_east')}: {east:.3f} m",f"{self.t('corrected_north')}: {north:.3f} m",f"{self.t('azimuth')}: {fmt(az)}",self.t("azimuth_rule"),""]
        lines += [f"{self.t('low_arc')}: {self.t('impossible')}",self.t("possible_reason")] if lo is None else [f"{self.t('low_arc')}: {fmt(lo)}"]
        lines += [f"{self.t('high_arc')}: {self.t('impossible')}"] if hi is None else [f"{self.t('high_arc')}: {fmt(hi)}"]
        self.set_text(self.r2,"\n".join(lines))
    def mode3(self):
        f=self.tab3; f.columnconfigure(0,weight=1); f.rowconfigure(2,weight=1)
        ttk.Label(f,text=self.t("mode3_title"),justify=tk.LEFT,wraplength=980).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=self.t("input")); inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8); inp.columnconfigure(3,weight=1)
        self.labent(inp,self.t("step"),self.m3step,0,0); ttk.Button(inp,text=self.t("generate"),command=self.table,width=14).grid(row=0,column=2,sticky="w",padx=8,pady=10)
        lf=ttk.LabelFrame(f,text=self.t("tab_mode3")); lf.grid(row=2,column=0,sticky="nsew",padx=14,pady=8); lf.rowconfigure(0,weight=1); lf.columnconfigure(0,weight=1)
        self.r3=tk.Text(lf,wrap=tk.NONE); self.r3.grid(row=0,column=0,sticky="nsew",padx=(8,0),pady=8)
        sy=ttk.Scrollbar(lf,orient=tk.VERTICAL,command=self.r3.yview); sx=ttk.Scrollbar(lf,orient=tk.HORIZONTAL,command=self.r3.xview); sy.grid(row=0,column=1,sticky="ns",padx=(0,8),pady=8); sx.grid(row=1,column=0,sticky="ew",padx=(8,0),pady=(0,8)); self.r3.configure(yscrollcommand=sy.set,xscrollcommand=sx.set); self.table()
    def table(self):
        try: step=i_step(self.m3step.get())
        except Exception: return messagebox.showerror(self.t("input_error"),f"{self.t('step')} {self.t('must_number')}")
        if step<=0:return messagebox.showerror(self.t("input_error"),f"{self.t('step')} {self.t('must_positive')}")
        lines=[self.t("table_header"),f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s",self.t("same_height_condition"),"",f"{self.t('distance'):>12} | {self.t('low_arc'):>18} | {self.t('high_arc'):>18}","-"*60]
        d=0
        while d<=1000:
            if d==0: lo,hi="0.000°","-"
            else:
                a,b=low_ang(d,0,self.current_velocity),high_ang(d,0,self.current_velocity); lo=self.t("impossible") if a is None else f"{a:.3f}°"; hi=self.t("impossible") if b is None else f"{b:.3f}°"
            lines.append(f"{d:12d} | {lo:>18} | {hi:>18}"); d+=step
        if hasattr(self,"r3"): self.set_text(self.r3,"\n".join(lines))
    def mode4(self):
        f=self.tab4; f.columnconfigure(0,weight=1); f.rowconfigure(2,weight=1)
        ttk.Label(f,text=f"{self.t('mode4_title')}\n{self.t('m4_hint')}",justify=tk.LEFT,wraplength=980).grid(row=0,column=0,sticky="ew",padx=14,pady=10)
        inp=ttk.LabelFrame(f,text=self.t("input")); inp.grid(row=1,column=0,sticky="ew",padx=14,pady=8)
        for i in range(8): inp.columnconfigure(i,weight=1)
        self.labent(inp,self.t("range_value"),self.m4r,0,0,14); self.labent(inp,self.t("angle_value"),self.m4a,0,2,14); self.labent(inp,self.t("sight_height"),self.m4sight,0,4,14)
        ttk.Label(inp,text=self.t("angle_unit")).grid(row=1,column=0,sticky="e",padx=8,pady=8)
        self.m4unitv=tk.StringVar(value=self.t(self.m4unit)); cb1=ttk.Combobox(inp,textvariable=self.m4unitv,values=[self.t("deg"),self.t("mil")],state="readonly",width=16); cb1.grid(row=1,column=1,sticky="w",padx=8,pady=8); cb1.bind("<<ComboboxSelected>>",self.m4_unit_changed)
        ttk.Label(inp,text=self.t("distance_type")).grid(row=1,column=2,sticky="e",padx=8,pady=8)
        self.m4typev=tk.StringVar(value=self.t(self.m4type)); cb2=ttk.Combobox(inp,textvariable=self.m4typev,values=[self.t("slant"),self.t("horizontal")],state="readonly",width=18); cb2.grid(row=1,column=3,sticky="w",padx=8,pady=8); cb2.bind("<<ComboboxSelected>>",self.m4_type_changed)
        ttk.Button(inp,text=self.t("calculate"),command=self.calc4,width=14).grid(row=1,column=5,sticky="w",padx=8,pady=8)
        self.r4=self.text_result(f)
    def m4_unit_changed(self,e=None): self.m4unit="deg" if self.m4unitv.get()==self.t("deg") else "mil"
    def m4_type_changed(self,e=None): self.m4type="slant" if self.m4typev.get()==self.t("slant") else "horizontal"
    def calc4(self):
        try:r=fnum(self.m4r.get(),self.t("range_value"),self.lang); a=fnum(self.m4a.get(),self.t("angle_value"),self.lang); sh=fnum(self.m4sight.get(),self.t("sight_height"),self.lang)
        except ValueError as e:return messagebox.showerror(self.t("input_error"),str(e))
        if r<=0:return messagebox.showerror(self.t("input_error"),f"{self.t('range_value')} {self.t('must_positive')}")
        h,hor,sl,rad=height_by_angle(r,a,self.m4unit,self.m4type)
        lines=[self.t("mode4_title"),"",f"{self.t('range_value')}: {r:.3f} m",f"{self.t('distance_type')}: {self.t(self.m4type)}",f"{self.t('angle_value')}: {a:.3f} {self.t(self.m4unit)}",f"radian: {rad:.6f}",f"{self.t('sight_height')}: {sh:.3f} m","",f"{self.t('height_from_optic')}: {h:.3f} m",f"{self.t('height_from_ground')}: {h+sh:.3f} m",f"{self.t('calc_horizontal')}: {hor:.3f} m",f"{self.t('calc_slant')}: {'N/A' if sl is None else f'{sl:.3f} m'}","",self.t("m4_hint")]
        self.set_text(self.r4,"\n".join(lines))
    def open_vel(self):
        w=tk.Toplevel(self.root); w.title(self.t("velocity_window_title")); w.geometry("420x220"); w.resizable(False,False)
        ttk.Label(w,text=f"{self.t('default_ags')}: {DEFAULT_VELOCITY:.3f} m/s\n{self.t('current_velocity')}: {self.current_velocity:.3f} m/s\n\n{self.t('temporary_velocity_hint')}",justify=tk.LEFT,wraplength=380).pack(anchor="w",padx=16,pady=14)
        f=ttk.Frame(w); f.pack(fill=tk.X,padx=16,pady=8); ttk.Label(f,text=self.t("new_velocity")).pack(side=tk.LEFT); v=tk.StringVar(value=f"{self.current_velocity:.3f}"); ttk.Entry(f,textvariable=v,width=14).pack(side=tk.LEFT,padx=8)
        def apply():
            try:nv=fnum(v.get(),self.t("new_velocity"),self.lang)
            except ValueError as e:return messagebox.showerror(self.t("input_error"),str(e),parent=w)
            if nv<=0:return messagebox.showerror(self.t("input_error"),f"{self.t('new_velocity')} {self.t('must_positive')}",parent=w)
            self.current_velocity=nv; self.update_vel(); self.table(); messagebox.showinfo(self.t("success"),f"{self.t('current_velocity')}: {nv:.3f} m/s",parent=w); w.destroy()
        ttk.Button(w,text=self.t("apply"),command=apply,width=12).pack(pady=12)
    def restore(self):
        self.current_velocity=DEFAULT_VELOCITY; self.update_vel(); self.table(); messagebox.showinfo(self.t("restored"),f"{self.t('current_velocity')}: {self.current_velocity:.3f} m/s")
    def manual(self):
        w=tk.Toplevel(self.root); w.title(self.t("manual_title")); w.geometry("780x640"); w.minsize(680,520)
        tx=tk.Text(w,wrap=tk.WORD); tx.pack(side=tk.LEFT,fill=tk.BOTH,expand=True,padx=(10,0),pady=10); sb=ttk.Scrollbar(w,orient=tk.VERTICAL,command=tx.yview); sb.pack(side=tk.RIGHT,fill=tk.Y,padx=(0,10),pady=10); tx.configure(yscrollcommand=sb.set); tx.insert(tk.END,self.manual_text()); tx.configure(state=tk.DISABLED)
    def manual_text(self):
        if self.lang=="zh": return f"""
塔科夫榴弹射击辅助说明书
============================================================
作者：{AUTHOR_NAME}
GitHub 仓库：{GITHUB_REPOSITORY}
地图坐标来源：{MAP_URL}

一、用途
------------------------------------------------------------
本工具用于《逃离塔科夫》的榴弹弹道辅助计算，支持距离高低差计算、坐标方位角计算、水平射表生成，以及通过角度或密位估算高度差。

二、默认 AGS 数据
------------------------------------------------------------
默认校准点：300m = 2.5°
重力加速度：g = 9.81 m/s²
默认等效初速：v = {DEFAULT_VELOCITY:.3f} m/s
该初速由游戏内实测校准点反推，不一定等于现实武器或游戏文件数据。

三、高低差规则
------------------------------------------------------------
高低差 = 目标高度 - 炮位高度。正数表示目标比炮位高，负数表示目标比炮位低。

四、坐标模式
------------------------------------------------------------
前者为炮位，后者为目标。程序根据坐标计算水平距离，并根据用户选择的真实方位修正方位角。
方位角定义：正北=0°，正东=90°，正南=180°，正西=270°。

五、射表模式
------------------------------------------------------------
生成 0~1000 米水平面射表。若存在高低差，请使用模式1或模式2，不要直接套用水平射表。

六、角度/密位测高模式
------------------------------------------------------------
该模式用于根据观测角度或瞄准镜密位估算目标相对观测点的高度差。
如果已知直线距离/斜距，使用：
    高度差 = 直线距离 × sin(角度)
如果已知水平距离，使用：
    高度差 = 水平距离 × tan(角度)
角度向上为正，向下为负。
如果使用密位/mrad，程序按 1 密位 = 0.001 弧度换算，即：
    弧度 = 密位 / 1000
瞄准镜离地高度会额外加到结果中，用于估算目标相对观测点地面的高度。

七、临时设置初速
------------------------------------------------------------
可通过“设置初速”临时修改炮弹速度。该设置不会保存，关闭程序后恢复默认。

八、地图链接
------------------------------------------------------------
坐标数据可从 Tarkov.dev 地图获取：{MAP_URL}

九、弹道公式
------------------------------------------------------------
同水平面射程公式：
    R = v² / g × sin(2θ)
有高低差弹道方程：
    h = x × tan(θ) - g × x² / [2 × v² × cos²(θ)]
解出：
    tan(θ) = [v² ± sqrt(v⁴ - g(gx² + 2hv²))] / gx
低弹道使用减号，高弹道使用加号。
"""
        return f"""
Tarkov Grenade Calculator Manual
============================================================
Author: {AUTHOR_NAME}
GitHub Repository: {GITHUB_REPOSITORY}
Map Coordinate Source: {MAP_URL}

1. Purpose
------------------------------------------------------------
This tool is a grenade ballistic calculator for Escape from Tarkov. It supports elevation calculation, coordinate-based azimuth calculation, horizontal firing table generation, and height estimation by angle or scope mil/mrad.

2. Default AGS Data
------------------------------------------------------------
Default calibration point: 300m = 2.5°
Gravity: g = 9.81 m/s²
Default equivalent velocity: v = {DEFAULT_VELOCITY:.3f} m/s
This value is calculated from in-game measured data and may not match real-world or internal game file data.

3. Height Difference Rule
------------------------------------------------------------
Height difference = target height - launcher height. Positive means higher, negative means lower.

4. Coordinate Mode
------------------------------------------------------------
First point is launcher, second point is target. The program calculates horizontal distance and uses selected real direction to correct azimuth.
Azimuth definition: North=0°, East=90°, South=180°, West=270°.

5. Firing Table Mode
------------------------------------------------------------
Generates a 0-1000m horizontal firing table. If height difference exists, use Mode 1 or Mode 2.

6. Angle/Mil Height Mode
------------------------------------------------------------
This mode estimates target height difference by observation angle or scope mil/mrad.
If slant range is known:
    height difference = slant range × sin(angle)
If horizontal range is known:
    height difference = horizontal range × tan(angle)
Positive angle means upward, negative means downward.
For mil/mrad, the program uses:
    radian = mil / 1000
Sight height above ground is added to estimate target height relative to observer ground.

7. Temporary Velocity
------------------------------------------------------------
Projectile velocity can be temporarily changed. It will not be saved after closing the program.

8. Map Link
------------------------------------------------------------
Coordinates can be obtained from Tarkov.dev maps: {MAP_URL}

9. Formula
------------------------------------------------------------
Same-height range:
    R = v² / g × sin(2θ)
Trajectory with height difference:
    h = x × tan(θ) - g × x² / [2 × v² × cos²(θ)]
Solving:
    tan(θ) = [v² ± sqrt(v⁴ - g(gx² + 2hv²))] / gx
Low arc uses minus, high arc uses plus.
"""
    @staticmethod
    def set_text(w,s):
        w.configure(state=tk.NORMAL); w.delete("1.0",tk.END); w.insert(tk.END,s); w.configure(state=tk.NORMAL)

def main():
    root=tk.Tk(); App(root); root.mainloop()
if __name__=="__main__": main()