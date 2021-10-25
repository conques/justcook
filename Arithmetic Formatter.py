def arithmetic_arranger(problems, responder=False):
    nums = ''
    dens = ''
    sums = ''
    respuestas = ""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for k in problems:
        l = (k.split(' '))
        num = l[0]
        op = l[1]
        den = l[2]
        if len(num) > 4 or len(den) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not num.isnumeric() or not den.isnumeric():
            return 'Error: Numbers must only contain digits.'
        if op == '+' or op == '-':
            length = max(len(num), len(den)) + 2
            top = str(num).rjust(length)
            bottom = op + str(den).rjust(length - 1)
            sum = ''
            for s in range(length):
                sum += '-'
            nums += top + '    '
            dens += bottom + '    '
            sums += sum + '    '
        else:
            return "Error: Operator must be '+' or '-'."
    nums = nums.rstrip()
    dens = dens.rstrip()
    sums = sums.rstrip()
    if responder:
        for k in problems:
          l = (k.split(' '))
          num = l[0]
          op = l[1]
          den = l[2]
          respuesta = ""
          if op == "+" :
            respuesta = (int(num) + int(den))
          else:
            respuesta = (int(num) - int(den))
          length = max(len(num), len(den)) + 2
          top = str(respuesta).rjust(length)
          respuestas += top + '    '
        respuestas = respuestas.rstrip()
        arranged_problems = nums + '\n' + dens + '\n' + sums + "\n" + respuestas
        return(arranged_problems)
    else:
        arranged_problems = nums + '\n' + dens + '\n' + sums
        return (arranged_problems)