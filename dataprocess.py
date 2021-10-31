from dataextract import get_row

def main():
    with open('data.csv', 'w') as f:
        data = [ ]
        dr = None
        for row in get_row():
            dt = row[1]
            if dr is None or len(dr) == 0 or dr[0] != dt:            
                dr = [ dt ]
                data.append(dr)
            dr.append(row[2])        
        for i, dr in enumerate(data):
            f.write(",".join(dr))
            f.write("\n")
    print "Done"

if __name__ == '__main__':
    main()
