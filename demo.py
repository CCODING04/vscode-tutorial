#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


def main():
    if random.randint(0, 10) >= 5:
        print("Hello VSCode!")
    else:
        print("Sad you're not")


if __name__ == "__main__":
    main()
