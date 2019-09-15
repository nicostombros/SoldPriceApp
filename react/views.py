from django.shortcuts import render
from .utils import load_data, get_color, get_relative_percentage

def home(request):
    context = {}
    price_ranges = [{'range':'0-5%','color':'p','index':'1'},
    {'range':'5-25%','color':'b','index':'2'},
    {'range':'25-75%','color':'g','index':'3'},
    {'range':'75-95%','color':'y','index':'4'},
    {'range':'95-100%','color':'r','index':'5'}]
    context['price_ranges'] = price_ranges
    f = load_data(file="sold-price-data.txt")
    price_counts = []
    x_subdivs, y_subdivs = 100, 100
    data = {x:{y:'' for y in range(y_subdivs)} for x in range(x_subdivs)}
    context.update({'x_subdivs':x_subdivs,'y_subdivs':y_subdivs})
    for num in range(len(f)):
        line = (f[num].decode('utf-8')).strip('\n')
        stripped = line.split()
        price_counts.append(int(stripped[2]))
        data[int(stripped[0])][int(stripped[1])] = {'price':int(stripped[2])}
    context['data'] = data
    pc = get_relative_percentage(arr=price_counts)
    context['pricing'] = pc
    for row,columns in data.items():
        for cell,info in columns.items():
            if info:
                info['color'] = get_color(p=info['price'],r=pc)
    res = {}
    res['total'] = len(price_counts)
    res['min'] = min(price_counts)
    res['max'] = max(price_counts)
    context['results'] = res
    return render(request,'index.html',context)
