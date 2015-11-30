import datetime
import json
import time
import traceback
import uuid

metrics_fn = '/tmp/%s-metrics.json' 
resulting_metrics_fn = '/tmp/%s-resulting_metrics.txt'
reference_metrics_fn = '%s-ref-metrics.json'

class MetricProcessor(object):
    def process_metrics(self, filename=metrics_fn):
        open(resulting_metrics_fn, 'w').close()
        with open(filename, "rt") as f:
            metrics = json.load(f)
        if filename == metrics_fn:
            import os
            os.rename(filename, metrics_new_fn % (str(datetime.datetime.now())))

        for metric in sorted(metrics.keys()):
            successes = 0
            failures = 0
            times = []
            for sample in metrics[metric]:
                if int(sample['result']):
                    successes += 1
                    times.append(float(sample['time']))
                else:
                    failures += 1
            if successes or failures:
                with open(resulting_metrics_fn, "at+") as res:
                    print >> res, "%s: success rate %s percent(s), " \
                                  "%s samples, %s seconds average time." % (metric,
                                                                            successes * 100.0 / (
                                                                            successes + failures),
                                                                            successes + failures,
                                                                            sum(times) / (successes + failures))
            else:
                with open(resulting_metrics_fn, "at+") as res:
                    print >> res, "%s: success rate %s percent(s), " \
                                  "%s samples, %s seconds average time." % (metric, 0, 0, 0)


class MetricGenerator:
    metrics = {}
    testcases = {}
    metrics_file_name = metrics_fn
    metric = None
    time = 0
    mg = None

    @classmethod
    def GetMetricGenerator(cls):
        if not cls.mg:
            cls.mg = MetricGenerator()
        return cls.mg

    def create_metric(self, metric):
        self.metric = metric
        if not self.metrics.has_key(self.metric):
            self.metrics[self.metric] = []
        #Post dummy metric sample that will be deleted in case of real success or failure.
        self.post_metric(metric, False, 0, ("Failed due to timeout", ))
        return self

    def post_metric(self, metric, value, time_t=0, details=()):
        if not self.metrics.has_key(self.metric):
            self.metrics[self.metric] = []
        metric_id = str(uuid.uuid4())
        self.metrics[self.metric].append(
            {'id': metric_id, 'name': metric, 'result': int(value), 'time': time_t, 'details': details})

        with open(self.metrics_file_name, "wt") as f:
            json.dump(self.metrics, f)

    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            formatted_exception = traceback.format_exception(exc_type, exc_val, exc_tb)
            self.post_metric(self.metric, False, -1, formatted_exception)
        else:
            self.post_metric(self.metric, True, time.time() - self.time, ())
