def iter_solo(x):
    def iterio(x):
        if not isinstance(x, dict):
            return str(x)
        result = []
        foo = ''
        for k, v in x.items():
            if not isinstance(v, dict):
                result.append(f"      {k}: {v}")
            if isinstance(v, dict):
                for kk, vv in v.items():
                    if not isinstance(vv, dict):
                        result.append(
                            f"{' '*6}{k}: {'{'}\n{' '*12}{kk}: {vv}\n{' '*8}{'}'}")
                    if isinstance(vv, dict):
                        for kkk, vvv in vv.items():
                            result.append(
                                f"{' '*6}{k}: {'{'}\n{' '*12}{kk}: {'{'}\n{' '*16}{kkk}: {vvv}\n{' '*12}{'}'}\n{' '*8}{'}'}")
        result = sorted(result, key=lambda x: x[5:])
        for i in result:
            foo += f"  {str(i)}\n"
        return f"{'{'}\n{foo}    {'}'}"
    return iterio(x)
