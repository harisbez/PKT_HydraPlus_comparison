import pickle


def print_results_line(model_name='Receiver', transfer_set='-', pickle_path='', eval_set='cifar10'):
    with open(pickle_path, 'rb') as f:
        results = pickle.load(f)

    line = model_name + ' & ' + transfer_set + ' '
    # cifar10
    res = results[eval_set]
    line += '& ${%3.2f}$ ' % (100 * res['map'])
    line += '& ${%3.2f}$ ' % (100 * res['raw_precision'][9])  # top-10
    line += '& ${%3.2f}$ ' % (100 * res['raw_precision'][19])  # top-20
    line += '& ${%3.2f}$ ' % (100 * res['raw_precision'][49])  # top-50
    line += '& ${%3.2f}$ ' % (100 * res['raw_precision'][99])  # top-100
    line += '& ${%3.2f}$ ' % (100 * res['raw_precision'][199])  # top-200
    line += ''

    print(line, '\\\\')

def print_results_line_ece_error(model_name='Receiver', pickle_path='', eval_set='cifar10'):
    with open(pickle_path, 'rb') as f:
        results = pickle.load(f)

    line = model_name + ' & '
    # cifar10
    res = results[eval_set]
    line += '& ${%3.2f}$ ' % (res['ece'])
    line += '& ${%3.2f}$ ' % (res['error'])
    line += ''

    print(line, '\\\\')


def print_exp1_table(eval_set='cifar10'):
    print("--------------")

    print_results_line(model_name='Student', transfer_set='-',
                       pickle_path='exp_cifar/results/new/tiny_cifar10_baseline.pickle', eval_set=eval_set)
    print_results_line(model_name='Teacher', transfer_set='-',
                       pickle_path='exp_cifar/results/new/resnet18_cifar10_baseline.pickle', eval_set=eval_set)
    print("--------------")

    print_results_line(model_name='Distill', transfer_set='-',
                       pickle_path='exp_cifar/results/new/cifar_tiny_resnet18_cifar10_distill_' + eval_set + '.pickle', eval_set=eval_set)

    # print("--------------")
    print_results_line(model_name='HINT (rand)', transfer_set='-',
                       pickle_path='exp_cifar/results/new/cifar_tiny_resnet18_cifar10_hint__' + eval_set + '.pickle', eval_set=eval_set)
    print_results_line(model_name='HINT (optimized)', transfer_set='-',
                       pickle_path='exp_cifar/results/new/cifar_tiny_resnet18_cifar10_hint_optimized__' + eval_set + '.pickle', eval_set=eval_set)
    print_results_line(model_name='KT', transfer_set='-',
                       pickle_path='rexp_cifar/results/new/cifar_tiny_resnet18_cifar10_kt_' + eval_set + '.pickle', eval_set=eval_set)

def print_exp1_table_ece_error(eval_set='cifar10'):
    print("--------------")

    print_results_line_ece_error(model_name='Student',
                       pickle_path='exp_cifar/results/new/tiny_cifar10_baseline.pickle', eval_set=eval_set)
    print_results_line_ece_error(model_name='Teacher',
                       pickle_path='exp_cifar/results/new/resnet18_cifar10_baseline.pickle', eval_set=eval_set)
    print("--------------")



if __name__ == '__main__':
    print_exp1_table(eval_set='cifar10')
