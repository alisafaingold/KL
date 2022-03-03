from ExecutionUtils import *
from KarmaLego_Framework.RunKarmaLego import runKarmaLego

def run_kl(bins, discrstization, max_gap, support):
    classes = [0,1]
    num_rel = 7

    path_prefix = '/home/alisaf/alisaKL/Tali/filter_entities/3_weeks/equal-width_2_1_windows_filter'
    out = f'{path_prefix}/max_gap_{max_gap}_min_sup_{support}_rel_{num_rel}'
    for c in classes:
        if not os.path.exists(f"{out}/TIRPs/class_{c}/"):
            os.makedirs(f"{out}/TIRPs/class_{c}/")

        runKarmaLego(time_intervals_path=f'{path_prefix}/KL-class-{c}.0.txt',
                     min_ver_support=support,
                     num_relations=num_rel,
                     skip_followers=True,
                     max_gap=max_gap,
                     label=0,
                     max_tirp_length=5,
                     num_comma=2,
                     need_one_sized=True,
                     semicolon_end=True,
                     output_path=f'{out}/TIRPs/class_{c}',
                     processes_num=10)



def my_parameters():
    bins = 2
    discrstization = discretization_shortcuts('ew')
    max_gap = 14
    support = 0.7
    return bins, discrstization, max_gap, support

if __name__ == '__main__':
    entities = 'filter'
    bins, discrstization, max_gap, support = my_parameters()
    prefix_matrix = run_kl(bins, discrstization, max_gap, support)
