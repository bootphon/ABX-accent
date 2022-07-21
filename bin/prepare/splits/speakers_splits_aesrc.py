import os
import librosa

def isMale(path):
    with open(path, 'r') as file:
        s = file.read()
    l = s.split()
    if 'Male' in l :
        return 1
    else:
            return 0


def split(path):
    male = []
    female = []
    speakers = os.listdir(path)
    for spk in speakers:
        if os.path.isdir(os.path.join(path, spk)):
            metadata = os.listdir(os.path.join(path, spk))[0]
            grp = metadata[:6]
            if isMale(os.path.join(path, spk, metadata)) :
                male.append(grp)
            else:
                female.append(grp)
    return male, female
        
def length_list(path, list):
    res_dict = {}
    for spk in list:
        spk_path = os.path.join(path, spk)
        res_dict[spk] = spk_length(spk_path)
    return res_dict

def spk_length(path):
    files = os.listdir(path)
    length = 0
    for file in files :
        if file[-4:] == '.wav' :
            file_path = os.path.join(path, file)
            arr, sr = librosa.load(file_path)
            length += len(arr)/sr
    return length
    
def output_txt(D, outpath, name):
    keys = sorted(D, key=lambda x: D[x] if D[x] >= 60*7 else max(D.values()) + D[x])
    
    with open(os.path.join(outpath, name + '_test'), 'w') as f:
        for key in keys[:6]:
            f.write(key)
            f.write('\n')
            
    with open(os.path.join(outpath, name + '_dev'), 'w') as f:
        for key in keys[6:12]:
            f.write(key)
            f.write('\n')
    
    with open(os.path.join(outpath, name + '_train'), 'w') as f:
        for key in keys[12:]:
            f.write(key)
            f.write('\n')
    
if __name__ == '__main__':
    P = "/scratch1/data/raw_data/AESRC/Datatang-English/data"
    accents = os.listdir(P)
        
    American_M = ['G00007', 'G00550', 'G00904', 'G01159', 'G01167', 'G01275', 'G01302', 'G01394', 'G01405', 'G01451', 'G01459', 'G01469', 'G01622', 'G01880', 'G01882', 'G12232', 'G12268', 'G20071', 'G20258', 'G20537', 'G20579', 'G20588', 'G20681', 'G20714', 'G20761', 'G20785', 'G20792', 'G20795', 'G20939', 'G30361', 'G30592', 'G30750', 'G30854']

    American_F = ['G00473', 'G00916', 'G01047', 'G01086', 'G01300', 'G01390', 'G01415', 'G01519', 'G01561', 'G01612', 'G01897', 'G10208', 'G10948', 'G11044', 'G11139', 'G11239', 'G11322', 'G11333', 'G11350', 'G11351', 'G11388', 'G11814', 'G11878', 'G12153', 'G12175', 'G12178', 'G12272', 'G12290', 'G20218', 'G20289', 'G20291', 'G20549', 'G20684', 'G30157', 'G30201', 'G30260', 'G40003']

    British_M = ['G00009', 'G00011', 'G00024', 'G00025', 'G00027', 'G00030', 'G00034', 'G00039', 'G00677', 'G00762', 'G00790', 'G00808', 'G00820', 'G00825', 'G00829', 'G00913', 'G01101', 'G01191', 'G01287', 'G01337', 'G01457', 'G01634', 'G01673', 'G01736', 'G01802', 'G01807', 'G01814', 'G10031', 'G10207', 'G10261', 'G10313', 'G10412', 'G10431', 'G10537', 'G10563', 'G10705', 'G10805', 'G10863', 'G10951', 'G10982', 'G10996', 'G11032', 'G11098', 'G11533', 'G11790', 'G20366', 'G21446', 'G21705', 'G30173', 'G41815']

    British_F = ['G00016', 'G00456', 'G00572', 'G00600', 'G00659', 'G00838', 'G00852', 'G00911', 'G00919', 'G00926', 'G01055', 'G01066', 'G01094', 'G01137', 'G01196', 'G01221', 'G01239', 'G01263', 'G01493', 'G01512', 'G01518', 'G01639', 'G01834', 'G01847', 'G10006', 'G10160', 'G10348', 'G10582', 'G10949', 'G11124', 'G11517', 'G11625', 'G11739', 'G20779', 'G31003', 'G31640', 'G40216', 'G40281', 'G40517', 'G41725', 'G60862', 'G61363']

    Canadian_M = ['G00073', 'G00117', 'G00165', 'G00171', 'G00211', 'G00261', 'G00267', 'G00351', 'G00357', 'G00364', 'G00368', 'G00407', 'G00410', 'G00411', 'G10019', 'G10032', 'G10133', 'G10206', 'G20060', 'G20113', 'G20149']

    Canadian_F = ['G00086', 'G00087', 'G00166', 'G00198', 'G00219', 'G00245', 'G00247', 'G00265', 'G00353', 'G00358', 'G00367', 'G00372', 'G00414', 'G10029', 'G10227', 'G10231', 'G10253', 'G20078', 'G30140', 'G30181', 'G30189', 'G70160']

    Chinese_M = ['G00021', 'G00251', 'G00397', 'G00427', 'G00511', 'G00541', 'G00571', 'G00594', 'G00853', 'G00918', 'G00983', 'G01263', 'G01268', 'G01298', 'G01372', 'G01377', 'G10224', 'G10932', 'G11021', 'G11033', 'G11168', 'G11235', 'G30104', 'G30795', 'G30798', 'G61365']

    Chinese_F = ['G00183', 'G00190', 'G00326', 'G00340', 'G00672', 'G00916', 'G00992', 'G01088', 'G01170', 'G01335', 'G01400', 'G01424', 'G10443', 'G10540', 'G10635', 'G11186', 'G12006', 'G20608', 'G21393', 'G30421', 'G30627', 'G40755', 'G61345', 'G70389']

    Indian_M = ['G00906', 'G00945', 'G00964', 'G00988', 'G01003', 'G01006', 'G01020', 'G01034', 'G01129', 'G01502', 'G01525', 'G01542', 'G01565', 'G01586', 'G0235', 'G0248', 'G0735', 'G0760', 'G0768', 'G1757']

    Indian_F = ['G00821', 'G00822', 'G00823', 'G00826', 'G00833', 'G00834', 'G00840', 'G00862', 'G00892', 'G01146', 'G01174', 'G01200', 'G01233', 'G01260', 'G01430', 'G01473', 'G01485', 'G01501', 'G01566', 'G0249', 'G0563', 'G0774']

    Japenese_M = ['G00004', 'G00011', 'G00036', 'G00066', 'G00096', 'G00105', 'G00122', 'G00130', 'G00159', 'G00177', 'G00212', 'G00285', 'G00304', 'G00354', 'G00385', 'G00429', 'G10019', 'G10024', 'G10227', 'G10308', 'G10351', 'G20162', 'G50009']

    Japenese_F = ['G00020', 'G00040', 'G00041', 'G00077', 'G00080', 'G00086', 'G00088', 'G00117', 'G00119', 'G00125', 'G00129', 'G00145', 'G00156', 'G00164', 'G00336', 'G00386', 'G00477', 'G10056', 'G10241', 'G10252', 'G20012', 'G20055', 'G20194']

    Korean_M = ['G00059', 'G00081', 'G00088', 'G00179', 'G00213', 'G00220', 'G00276', 'G00281', 'G00397', 'G10020', 'G10085', 'G10095', 'G10128', 'G10142', 'G10257', 'G10297', 'G10305', 'G10323', 'G10343', 'G20046', 'G20056', 'G20212', 'G20246']

    Korean_F = ['G00022', 'G00025', 'G00038', 'G00047', 'G00053', 'G00055', 'G00075', 'G00099', 'G00141', 'G00200', 'G00201', 'G00203', 'G10027', 'G10029', 'G10031', 'G10060', 'G10104', 'G10122', 'G10157', 'G10180', 'G10185', 'G20061', 'G20165']

    Portugese_M = ['G00471', 'G00504', 'G00510', 'G00512', 'G00516', 'G00521', 'G00527', 'G00537', 'G00561', 'G00565', 'G00578', 'G00603', 'G00636', 'G00643', 'G00675', 'G00719', 'G00787', 'G10465', 'G10988', 'G20493', 'G20532', 'G20539', 'G30534', 'G30647', 'G40538', 'G40582']

    Portugese_F = ['G00004', 'G00505', 'G00550', 'G00577', 'G00600', 'G00628', 'G00642', 'G00644', 'G00663', 'G00680', 'G00693', 'G00734', 'G00735', 'G00963', 'G00965', 'G01027', 'G10491', 'G10496', 'G10503', 'G10618', 'G10640', 'G10656', 'G10657', 'G10746', 'G20599', 'G50494', 'G60478']

    Russian_M = ['G00021', 'G00034', 'G00075', 'G00086', 'G00173', 'G00192', 'G00196', 'G00216', 'G00245', 'G00270', 'G00271', 'G00341', 'G00424', 'G00440', 'G00494', 'G00558', 'G10012', 'G10063', 'G10416', 'G20045']

    Russian_F = ['G00033', 'G00102', 'G00108', 'G00121', 'G00163', 'G00244', 'G00247', 'G00248', 'G00263', 'G00273', 'G00339', 'G00360', 'G00363', 'G00430', 'G00435', 'G00439', 'G00473', 'G10006', 'G10156', 'G10158', 'G10310']

    Spanish_M = ['G01714', 'G01715', 'G01721', 'G01778', 'G01790', 'G01885', 'G01965', 'G01968', 'G10158', 'G10227', 'G10235', 'G11701', 'G11722', 'G20407', 'G20575', 'G21668', 'G30222', 'G31441', 'G31638', 'G31680', 'G40571', 'G41673']

    Spanish_F = ['G00714', 'G01688', 'G01764', 'G01773', 'G01779', 'G01873', 'G01878', 'G01881', 'G01887', 'G01894', 'G01897', 'G01925', 'G01928', 'G01930', 'G01933', 'G01934', 'G11777', 'G20196', 'G21515', 'G31502', 'G51566', 'G51624']
    
    american_path = "/scratch1/data/raw_data/AESRC/Datatang-English/data/American English Speech Data"
    out_path = '/scratch2/rsanroman/Workspace/AESRC_splits/splits'
    
    gender_index = {'American English Speech Data': [American_M, American_F], 'Canadian English Speech Data': [Canadian_M, Canadian_F], 'Indian English Speech Data': [Indian_M, Indian_F], 'Korean Speaking English Speech Data': [Korean_M, Korean_F], 'Russian Speaking English Speech Data': [Russian_M, Russian_F], 'British English Speech Data': [British_M, British_F], 'Chinese Speaking English Speech Data': [Chinese_M, Chinese_F],'Japanese Speaking English Speech Data':  [Japenese_M, Japenese_F], 'Portuguese Speaking English Speech Data': [Portugese_M, Portugese_F], 'Spanish Speaking English Speech Data': [Spanish_M, Spanish_F]}
    
    Done = []
    
    for accent in accents:
        if accent not in Done:
            data_path = os.path.join(P, accent)
            D = length_list(data_path, gender_index[accent][0])
            output_txt(D, out_path, accent.split()[0] + '_M')
            D = length_list(data_path, gender_index[accent][1])
            output_txt(D, out_path, accent.split()[0] + '_F')
        
    
    
    #print(spk_length(os.path.join(american_path, American_M[0])))
    
    
    

