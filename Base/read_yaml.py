import yaml,os


class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+'Data'+os.sep+filename

    def read_yaml(self):
        with open(self.filepath,'r',encoding='utf-8')as f:
            return yaml.load(f)
    def read_yaml02(self):
        with open ('../Data/login.yaml','r',encoding='utf-8') as f:
            return yaml.load(f)

if __name__ == '__main__':

    """  最终要的格式:
         return [('18610453007','12345'),(),()]
    """
    datas = ReadYaml('login.yaml').read_yaml02()
    print(datas)
    arrs = []
    for data in datas.values():
        arrs.append((data.get('username'),data.get("password")))
    print(arrs)
