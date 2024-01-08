import sys
import random

def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def assign_to_cluster(data, centers):
    clusters = [[] for _ in range(len(centers))]
    for point in data:
        closest_center = min([(i, euclidean_distance(point, centers[i])) for i in range(len(centers))], key=lambda x: x[1])[0]
        clusters[closest_center].append(point)
    return clusters

def find_centers(clusters):
    centers = []
    for cluster in clusters:
        x = sum(point[0] for point in cluster) / len(cluster)
        y = sum(point[1] for point in cluster) / len(cluster)
        centers.append((x, y))
    return centers

def kmeans(k, data):
    centers = random.sample(data, k)
    while True:
        clusters = assign_to_cluster(data, centers)
        new_centers = find_centers(clusters)
        if new_centers == centers:
            break
        centers = new_centers
    return clusters

def read_file(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split())
            data.append((x, y))
    return data

def output(clusters):
    with open("output.txt", 'w') as f:
        for i, cluster in enumerate(clusters):
            for point in cluster:
                f.write(f'{point[0]}\t{point[1]}\t{i+1}\n')

if __name__ == '__main__':
    k = int(sys.argv[1])
    data = read_file(sys.argv[2])
    clusters = kmeans(k, data)
    output(clusters)