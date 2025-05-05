from glob import glob
import solve

for instance in glob('./*.txt'):
    print()
    print('=' * 4, instance.replace('./', '').replace('.txt', ''), '=' * 4)
    solve.main(instance)
    print('=' * 20)
    print()