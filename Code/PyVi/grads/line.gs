*INPUT: outputdir, name, lat, lon, gmtdiff, pname, pbez, tend, abez, para1:col1, para2:col2, para3:col3, 0
*grads -b -a 1.333 -x -c "run /home/tibyte/Desktop/PyVi/grads/line.gs /home/tibyte/Desktop/PyVi/output/ Berlin 52 12 1 tql Wassersaeule 48 [DU] tql/100:32 0"
*grads -b -a 1.333 -x -c "run /home/tibyte/Desktop/PyVi/grads/line.gs /home/tibyte/Desktop/PyVi/output/ Berlin 52 12 1 t2m_tql Regen_Temperatur last [DU]_[C] tql/100:32 t2m-273:47 0"

function main(args)
  _server = "http://opendap.nccs.nasa.gov:80/dods/GEOS-5/fp/0.25_deg/fcast/tavg1_2d_slv_Nx.latest"
  iter = 0
  _arguments = 0
  while(iter < 5 | subwrd(args,iter+1) != "0")
    _arguments.iter = subwrd(args,iter+1)
    iter = iter + 1
  endwhile
  connect(_server)
  colorSetup()
  reset()

  time.1 = "32"
  time.2 = "72"
  time.3 = "last"
  count = 1
  'set t 1 'time.count
  drawTitle(_arguments.1' '_arguments.6,_arguments.8)
  reset()
  'set lat '_arguments.2
  'set lon '_arguments.3
  pc = 9
  _p = ""
  _c = ""
  _n = iter - pc
  while (pc < iter)
    colon = 0 
    col = 0
    found = 0
    while (found != 1 & colon < strlen(_arguments.pc))
      colon = colon + 1
      if (substr(_arguments.pc,colon,1) = ":")
        found = 1
      endif
    endwhile
    col = substr(_arguments.pc,colon+1,strlen(_arguments.pc)-colon+1)
    para = substr(_arguments.pc,1,colon-1)
    drawSingle(para,col)
    p1 = iter - pc
    _p.p1 = para
    _c.p1 = col
    pc = pc + 1
  endwhile
  saveDisplay(_arguments.0,_arguments.1,_arguments.5,time.count)
  'clear'

  count = 2
  while (count <= 3)
    n = 1
    'set t 1 'time.count
    drawTitle(_arguments.1' '_arguments.6,_arguments.8)
    reset()
    while(n <= _n)
      drawSingle(_p.n,_c.n)
      n = n+1
    endwhile
    saveDisplay(_arguments.0,_arguments.1,_arguments.5,time.count)
    'clear'
    count = count + 1
  endwhile
return

function connect(server)
  'sdfopen 'server
return

function reset()
  'set strsiz 17'
  'set font 1'
  'set digsiz 0.02'
  'set grads off'
  'set cthick 9'
  'set csmooth on'
  'set gxout shaded'
  'set cmark 0'
  'set timelab on'
  'set gridln 17'
return

function drawSingle(arg, col)
  say arg' 'col
  'set ccolor 'col
  'd 'arg
return

function drawTitle(title, yAxis)
  'query time'
  res = subwrd(result,5)
  'set strsiz 0.25'
  'set string 1 c 15 0 '
  'draw string 5.5 8.1 Prognose 'title' bis 'substr(res,7,5)
  'set strsiz 0.21'
  'set string 1 c 15 0 '
  'draw string 6.2 0.27 Zeit [Tag]' 
  'set string 1 c 15 90 '
  'draw string 0.75 4.25 'yAxis
return

function colorSetup()
    'set rgb 99   255  255  255'
    'set rgb 98     0    0    0'
    'set rgb  29   15    0  100'
    'set rgb  30   35   50  100'
    'set rgb  31   35   50  140'
    'set rgb  32   35   80  160'
    'set rgb  33   35  125  180'
    'set rgb  34  100  200  225'
    'set rgb  35  150  225  250'
    'set rgb  36  175  240  250'
    'set rgb  37  200  250  250'
    'set rgb  38  210  250  230'
    'set rgb  39  230  250  210'
    'set rgb  40  255  255  175'
    'set rgb  41  255  220  175'
    'set rgb  42  255  200  150'
    'set rgb  43  255  200    0'
    'set rgb  44  255  150    0'
    'set rgb  45  255  100    0'
    'set rgb  46  255   50    0'
    'set rgb  47  200    0    0'
    'set rgb  48  175    0    0'
    'set rgb  49  125    0    0'
    'set rgb  50   75    0    0'
    'set rgb  17   17   17   17'
return

function saveDisplay(dir, name, pbez, tend)
    'printim 'dir%name'/'pbez'/'pbez'_'tend'.jpg x800 y600'
    say name'/'pbez'/'pbez'_'tend'.jpg'
return