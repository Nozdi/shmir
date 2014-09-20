from os import (
    fork,
    waitpid,
    execl,
    path,
)
from zipfile import ZipFile

from shmir.contextmanagers import mfold_path
from shmir.async import task
from shmir.settings import (
    MFOLD_PATH,
)


def zipped_mfold(task_id, files, tmp_dirname):
    zipname = "{}.zip".format(task_id)

    with ZipFile(zipname, 'w') as mfold_zip:
        for filename in files:
            mfold_zip.write(
                filename, "{}/{}".format(*filename.split('/')[-2:])
            )

    result = path.join(tmp_dirname, zipname)

    return result


def execute_mfold(path_id, sequence, zip_file=True):
    with mfold_path(path_id) as tmp_dirname:
        with open('sequence', "w") as f:
            f.write(sequence)

        pid = fork()

        if pid == 0:
            execl(MFOLD_PATH, 'mfold', 'SEQ=sequence')

        process_id, status = waitpid(pid, 0)
        # Status in 0 - 255
        status = (status & 0xff00) >> 8

        if status == 0:
            result = map(
                lambda mfold_path: path.join(
                    tmp_dirname, mfold_path.format('sequence')
                ),
                ["{}_1.pdf", "{}_1.ss"]
            )

            if zip_file:
                result = zipped_mfold(path_id, result, tmp_dirname)
        else:
            result = {
                'status': 'error',
                'error': "No foldings",
            }

    return result


@task(bind=True)
def delegate_mfold(self, sequence):
    """
    Executes mfold in order to generate appropriate files
    """
    return execute_mfold(self.request.id, sequence)