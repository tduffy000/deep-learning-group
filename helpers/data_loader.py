import os

class DatasetCreator:

    def __init__(self, root, disallowed=['.DS_Store', '']):
        self.root = root
        self.disallowed = disallowed

    @staticmethod
    def _is_image_file(f_name):
        return f_name.endswith('.png') or f_name.endswith('.jpeg') or f_name.endswith('.jpg')

    def get_image_files(self, n=None):
        self.all_image_files = {}
        self.categorical_mapping = {}
        self.n_samples = 0
        for path, _, files in os.walk(self.root):
            label = path.split('/')[-1]
            for f in files:
                if self._is_image_file(f):
                    self.all_image_files[label] = self.all_image_files.get(label, []) + [os.path.join(path, f)]
        if n is None:

            for label, file_list in self.all_image_files.items():
                # update categorical mapping
                self.categorical_mapping[label] = len(self.categorical_mapping)
                # update total sample count
                self.n_samples += len(file_list)

            return self.n_samples, self.all_image_files
        else:
            image_files = {}
            top_n_labels = [ t[0] for t in sorted([(k, len(v)) for k,v in self.all_image_files.items()], key=lambda x: -x[1])[:n]]
            for label in top_n_labels:
                image_files[label] = self.all_image_files[label]
                self.categorical_mapping[label] = len(self.categorical_mapping)
                self.n_samples += len(self.all_image_files[label])
            return self.n_samples, image_files

    def get_label(self, mapped):
        assert(isinstance(mapped, int))
        for k, v in self.categorical_mapping.items():
            if mapped == v:
                return k
