
'''index visualization
07:05:45AM'
0123456789
'''

s = '12:05:45AM'

def timeConversion(s):
    am_or_pm = s[-2:]
    ss = s[6:8]
    mm = s[3:5]
    hh = s[:2]
    m_hh = hh
    print(am_or_pm)
    print(ss)
    print(mm)
    print(hh)
    
    if am_or_pm == 'PM' and hh != '12':
      m_hh = str(int(hh) + 12)
      print(m_hh)
    if hh == '12' and am_or_pm == 'AM':
      m_hh = '00'

    result = m_hh + ':' + mm + ':' + ss
    print(result)
    return result




timeConversion(s)
