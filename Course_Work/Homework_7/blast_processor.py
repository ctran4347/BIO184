import sys,os
os.system("cls")
def mismatch_filter(hit_string):
    mismatch_count=int(hit_string.split("\t")[4])
    return mismatch_count < 20

def comment_filter(line):
    return not line.startswith('#')

def get_percent(hit_string):
    return float(hit_string.split("\t")[2])

def get_subject(hit_string):
    return hit_string.split("\t")[1]

def subject_filter(hit_string):
    subject=hit_string.split("\t")[1]
    if sys.argv[2] in subject:
        return True
    else:
        return False

def start_ratio(hit_string):
    query_start=int(hit_string.split("\t")[6])
    hit_length=int(hit_string.split("\t")[3])
    return query_start / hit_length

hits=list(filter(comment_filter,open(sys.argv[1])))
few_mismatches=filter(mismatch_filter,hits)
print("Fewer than 20 mismatches:","\n" + str(len(list(few_mismatches))))
sorted_by_percent=sorted(hits,key=get_percent)
low_hits=sorted_by_percent[:10]
print("Ten lowest percentage identical position matches:")
for low_hit in map(get_subject,low_hits):
    print(low_hit)

subject_hits=filter(subject_filter,hits)
print(str(sys.argv[2]),"query fractional start position:")
for query_fractional in map(start_ratio,list(subject_hits)):
    print(query_fractional)

#python blast_processor.py blast_result.txt COX1





