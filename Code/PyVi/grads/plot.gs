*INPUT: outdir, name, lat, lon, area, gmt, title, frontpara, backpara, color

function main(args)
  _server = "http://opendap.nccs.nasa.gov:80/dods/GEOS-5/fp/0.25_deg/fcast/tavg1_2d_slv_Nx.latest"
  connect(_server)
  _outdir = subwrd(args,1)
  _name = subwrd(args,2)
  _lat = subwrd(args,3)
  _lon = subwrd(args,4)
  _area = subwrd(args,5)
  _gmt = subwrd(args,6)
  _title = subwrd(args,7)
  _frontpara = subwrd(args,8)
  _backpara = subwrd(args,9)
  _color = subwrd(args,10)
  reset()

  focus(_lat, _lon, _area, _name)

  more = 1
  setTime("1 last")
  'query time'
  end = subwrd(result, 5)
  while (more >= 1)
    timeStamp = genPlot(_backpara, _title, more, _gmt, _frontpara, _name, _outdir, _color)
    more = more + 1
    if timeStamp = end
      more = 0
    endif
  endwhile



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

function focus(lat, lon, area, name)
    if name = "Europa"
        'set lat 30 69'
        'set lon -24 35'
        return
    endif
    if name = "Welt"
        'set lat -90 90'
        'set lon -170 170'
        return
    endif
    'set lat 'lat-area' 'lat+area
    'set lon 'lon-area' 'lon+area
return

function saveDisplay(file, num)
  if valnum(num) != 0
    len = math_strlen(num)
    if len = 3
      num = "0"num
    endif
    if len = 2
      num = "00"num
    endif
    if len = 1
      num = "000"num
    endif
  endif
  'printim 'file'_'num'.jpg x800 y600'
  say file'_'num'.jpg'
return

function timeCalc(oldTime, gmtdiff)
  setTime(oldTime + gmtdiff)
  'query time'
  res = subwrd(result,3)
  newTime = substr(res,1,5)
  setTime(oldTime)
return newTime

function calCalc(oldTime, diff)
  setTime(oldTime+diff)
  'query time'
  res = subwrd(result,3)
  newCal = substr(res,7,5)
  setTime(oldTime)
return newCal

function setTime(span)
    'set t 'span
return

*genPlot(_backpara, _title, more, _gmt, _frontpara, _name, _outdir, _color)
function genPlot(arg, title, time, gmt, dest, name, dir, color)
  setTime(time)
  'query time'
  begin = subwrd(result, 3)
  gmtZone = substr(begin, 1, 11)
  genTime = timeCalc(time, gmt)
  genDay = calCalc(time, gmt)
  drawLegend(arg, genTime" "title" am "genDay, name, color)
  file = dir%name%"/plot/"%dest%"/"%dest
  saveDisplay(file, time)
  new()
return begin

function drawLegend(arg, title, ort, color)
* Color Script
  ''color
* Color Script
  'set map 1 1 10'
  'set mpdset hires'
  'set grid off'
  'd 'arg
  _outdir'/../grads/cbarn.gs'
  'set strsiz 0.25'
  'set string 1 c 15 0 '
  'draw string 5.4 8.1 'title' um 'ort
  'set strsiz 0.21'
  'set string 1 c 15 0 '
  'draw string 5.6 0.45 Laengengrad' 
  'set string 1 r 15 90 '
  'draw string 0.5 5.5 Breitengrad'
  'set string 46 c'
  'draw string 5.5 4.25 *'
return

function new()
    'clear'
    reset()
return