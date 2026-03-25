# scripts/analyze_logs.py
import re
from collections import Counter
from datetime import datetime

def parse_log_file(filepath):
    """Parse learnloop.log and extract metrics"""
    metrics = {
        'total_requests': 0,
        'errors': 0,
        'avg_latency': 0,
        'agent_invocations': 0,
        'evaluations': 0,
    }

    with open(filepath, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                metrics['errors'] += 1
            if 'agent invocation' in line.lower():
                metrics['agent_invocations'] += 1
            if 'evaluation score' in line.lower():
                metrics['evaluations'] += 1
            metrics['total_requests'] += 1

    return metrics

if __name__ == '__main__':
    metrics = parse_log_file('logs/learnloop.log')
    print(f"Total Requests: {metrics['total_requests']}")
    print(f"Errors: {metrics['errors']}")
    print(f"Agent Invocations: {metrics['agent_invocations']}")
    print(f"Evaluations: {metrics['evaluations']}")
