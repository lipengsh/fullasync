#! /usr/bin/env bash
set -e

celery worker -A tasks.tasks -l info -Q main-queue -c 1
