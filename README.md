# Backie
A background task processor.

This repo is all about me figuring out how background task processors work.
The principle behind how they work is very simple; turn a tasks arguments to a string, store the string in a database of sorts, retrieve that string from the database at a later datetime and feed those arguments to the actual task to run.
Of course on top of that simple idea, these task processors go on and layer other useful features like; retries, periodic tasks, chaining of tasks etc.

### How to run
Putting it all together, lets run a redis server(using docker) in one terminal;

```
docker run -p 6379:6379 redis:5.0-alpine
```

And in another terminal we run the tasks;

```
python ecommerce_tasks.py
    task: 160491ba-a09f-4ea8-96f8-e3cf6ff7b580 succesfuly queued
```

In a third terminal run the workers;
```
python ecommerce_worker.py
    running task: 4ed63e42-f614-4093-a654-46211d5de8cf
    https://httpbin.org/24dkq40/example@example.org
    succesful run of task: 4ed63e42-f614-4093-a654-46211d5de8cf
```


### PS: Blog post coming soon.
