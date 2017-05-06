import sys, os
SalaryPerHour = input("Salário por Hora: ")
try:
    float(SalaryPerHour)
except:
    print("Erro: 'Salário por Hora' não é um valor valido.")
    sys.exit() 
WorkedHour = input("Horas trabalhadas: ")
try:
    float(WorkedHour)
except:
    print("Erro: 'Horas trabalhadas' não é um valor valido.")
    sys.exit() 
fSalaryPerHour = float(SalaryPerHour)
fWorkedHour = float(WorkedHour)
GrossSalary = fSalaryPerHour * fWorkedHour
IncomeTax = (GrossSalary/100)*11;
INSS = (GrossSalary/100)*8;
Syndicate=(GrossSalary/100)*5;
NetSalary = GrossSalary-IncomeTax-INSS-Syndicate
print("Salário Bruto: ", round(GrossSalary,2))
print("INSS: ", round(INSS,2))
print("Sindicato: ", round(Syndicate,2))
print("Salário Liquido: ", round(NetSalary,2))
os.system("pause")