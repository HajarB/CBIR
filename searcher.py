import numpy as np
import csv

class Searcher:
    def __init__(self, indexPath):
        self.indexPath = indexPath
        
    def chi2_distance(self, histA, histB, eps = 1e-10):
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                    for (a, b) in zip(histA, histB)])
        return d

    def search(self, queryFeatures, limit = 5):
        #initialize the dictionary of results
        results = {}
        #open the index file for reading
        with open(self.indexPath) as f:
            #initialize the CSV reader
            reader = csv.reader(f)

            for row in reader:
                #parse out the image ID and features, then compute the
                #chi-squared distance between the features in our index
                #and our query features
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)

                results[row[0]] = d
            
                
            f.close()

            #sort out the results so that the smaller distances are at
            #the fron of the list
            results = sorted([(v,k) for (k, v) in results.items()])
            

            return results[:limit]

