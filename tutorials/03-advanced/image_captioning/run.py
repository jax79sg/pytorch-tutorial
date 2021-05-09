import subprocess
from clearml import Task, Logger
t = Task.init(project_name="examples", task_name="image captioning")
t.set_base_docker(
    docker_cmd="nvcr.io/nvidia/pytorch:21.04-py3",
    docker_arguments="-e ENV=1",
    docker_setup_bash_script=['apt update', 'apt-get install -y build-essential','git clone https://github.com/pdollar/coco.git','cd coco/PythonAPI/','make','python setup.py build','python setup.py install']
)
t.execute_remotely(queue_name='single_gpu',exit_process=True)

print("PWD: ",end='')
subprocess.run(["pwd"])
subprocess.run(["ls","-ll"])
subprocess.run(["chmod", "+x", "download.sh"])
subprocess.run(["ls","-ll"])
subprocess.run("./download.sh",shell=True)

exec(open("build_vocab.py").read())
exec(open("resize.py").read())
exec(open("train.py").read())
