import sys
sys.path.append('./src')
import batch


def handler(event, context):
    return batch.mainCmd(event)
