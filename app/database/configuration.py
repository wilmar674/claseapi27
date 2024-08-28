#datos para la conexion a BD

dataBaseNme="gestorclm"
userNme="root"
userPassword=""
connectionport=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnetor://{userNme}:{userPassword}@{server}:{connectionport}/{dataBaseNme}"

print(dataBaseConnection)
