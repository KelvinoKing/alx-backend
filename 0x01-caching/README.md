# Caching Project

This project aims to implement various caching algorithms in Python, exploring concepts such as FIFO, LIFO, LRU, and MRU.

## Background Context

Caching is a critical technique in computer science used to store frequently accessed data in a faster storage location, enabling quicker access. This project provides hands-on experience with different caching strategies, helping to understand their implementations and trade-offs.

## Learning Objectives

By completing this project, learners will achieve the following objectives:

- Gain an understanding of caching systems.
- Familiarize with FIFO, LIFO, LRU, and MRU caching strategies.
- Implement caching algorithms in Python.

## Resources

To comprehend caching algorithms better, learners can refer to the following resources:

- Cache replacement policies - FIFO
- Cache replacement policies - LIFO
- Cache replacement policies - LRU
- Cache replacement policies - MRU
- Cache replacement policies - LFU

## Requirements

### Python Scripts

- All scripts will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Scripts should end with a new line.
- The first line of each script should be `#!/usr/bin/env python3`.
- All files must be executable.
- Code should follow PEP8 style guidelines (`pycodestyle` version 2.5).
- Documentation for all modules, classes, and functions is required.
- Documentations should be meaningful sentences explaining the purpose of the module, class, or method.
- A `README.md` file is mandatory and should be at the root of the project folder.

## Tasks

### 0. Basic dictionary

- Create a class `BasicCache` that inherits from `BaseCaching` and implements a basic caching system.
- This caching system doesn’t have a limit.
- Implement `put` and `get` methods as described in the task.

### 1. FIFO caching

- Create a class `FIFOCache` that inherits from `BaseCaching` and implements FIFO caching strategy.
- Implement `put` and `get` methods as described in the task.

### 2. LIFO caching

- Create a class `LIFOCache` that inherits from `BaseCaching` and implements LIFO caching strategy.
- Implement `put` and `get` methods as described in the task.

### 3. LRU caching

- Create a class `LRUCache` that inherits from `BaseCaching` and implements LRU caching strategy.
- Implement `put` and `get` methods as described in the task.

### 4. MRU caching

- Create a class `MRUCache` that inherits from `BaseCaching` and implements MRU caching strategy.
- Implement `put` and `get` methods as described in the task.

## Repository Information

- **GitHub repository:** [alx-backend](https://github.com/your-username/alx-backend)
- **Directory:** 0x01-caching

Refer to the respective files (`0-basic_cache.py`, `1-fifo_cache.py`, `2-lifo_cache.py`, `3-lru_cache.py`, `4-mru_cache.py`) in the repository for the implementations of each caching algorithm.
