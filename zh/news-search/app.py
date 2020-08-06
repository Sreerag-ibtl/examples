__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

import json
import os

import click
from jina.flow import Flow

workspace_path = '/tmp/jina/news/'

os.environ['TMP_WORKSPACE'] = workspace_path


def print_topk(resp):
    print(f'以下是相似的新闻内容:')
    for d in resp.search.docs:
        print(d)
        # for match in d.matches:
        #     item = match.text
        #     print('item: ', item)
        #     print('👉%s.............' % item['content'][:50])

def read_query_data(item):
    yield '{}'.format(json.dumps(item, ensure_ascii=False))


@click.command()
@click.option('--task', '-t', default='query')
@click.option('--top_k', '-k', default=5)
@click.option('--num_docs', '-n', default=100)
def main(task, top_k, num_docs):
    if task == 'index':
        data_fn = os.path.join(workspace_path, "pre_news2016zh_valid.json")
        flow = Flow().load_config('flow-index.yml')
        with flow:
            flow.index_lines(filepath=data_fn, size=num_docs, batch_size=32)

    elif task == 'query':
        flow = Flow().load_config('flow-query.yml')
        with flow:
            while True:
                content = input('请输入新闻内容: ')
                if not content:
                    break
                item = {'content': content}

                ppr = lambda x: print_topk(x)
                flow.search(read_query_data(item), callback=ppr, top_k=top_k)
    else:
        raise NotImplementedError(
            f'unknown task: {task}. A valid task is either `index` or `query`.')


if __name__ == '__main__':
    main()
