import subprocess
from clearml import Task, Logger
t = Task.init(project_name="examples", task_name="image captioning")
t.set_base_docker(
    docker_cmd="nvidia/cuda:10.2-devel-ubuntu18.04",
    docker_arguments="-e ENV=1",
    docker_setup_bash_script=['apt update', 'apt-get install -y build-essential','git clone https://github.com/pdollar/coco.git','cd coco/PythonAPI/','make','python setup.py build','python setup.py install']
)
t.execute_remotely(queue_name='single_gpu',exit_process=True)

subprocess.run(["chmod", "+x", "download.sh"])
subprocess.run(["./download.sh"])
subprocess.run(["pwd"])
subprocess.run(["ls"])
subprocess.run(["ls", "data"])

