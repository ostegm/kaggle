import yaml, datetime
creds = yaml.load(open('/home/ubuntu/credentials.yaml'))
kg_uname = creds['kaggle_user']
kg_pass = creds['kaggle_pass']

def create_submission_file(predictions, test_id, info):
    result1 = pd.DataFrame(predictions, columns=['ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT'])
    result1.loc[:, 'image'] = pd.Series(test_id, index=result1.index)
    now = datetime.datetime.now()
    subpath = './data/submissions/'
    sub_file = subpath + 'sub_' + info  + '_' + str(now.strftime("%Y-%m-%d-%H-%M")) + '.csv'
    order = ['image', 'ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']
    result1 = result1[order]
    result1.to_csv(sub_file, index=False)
    return result1, sub_file

def do_clip(arr, mx): 
    return np.clip(arr, (1-mx)/9, mx)


def gen_submission_file(fname, comp, info):
    comp = 'the-nature-conservancy-fisheries-monitoring'
    cmd = "kg submit {} -c {} -u {} -p {} -m '{}'".format(fname, comp, kg_uname, kg_pass, info)
    return cmd