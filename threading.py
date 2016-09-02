Summary | Date

from datetime import timedelta, date, datetime
import pickle

#http://stackoverflow.com/questions/6568007/how-do-i-save-and-restore-multiple-variables-in-python

def savethreads(self, list, queue):
	# Saving the objects:
	with open('threads.pickle', 'wb') as f:
		pickle.dump([list, queue], f)

def readthreads(self):
	# Getting back the objects:
	with open('threads.pickle', 'rb') as f:
		list, queue = pickle.load(f)
		return list, queue

list, queue = self.readthreads()
...
self.savethreads(list, queue)

queue = [
	["fold x(-x) from brd","url","dest",date,[imgs]]
	]

processfile
self.queue.append([summary,url,dest,"New",imgs])

timeout
updated = datetime.datetime.today()
q[i][3] = updated

http://stackoverflow.com/questions/16934087/how-to-do-background-task-in-gtk3-python/16949065#16949065

import threading
import gobject

    def main(self):

        #gobject.timeout_add(200, self.update_progress)
		

    # this will get periodically called in the GUI thread
    def update_progress(self, lbl, progress):
		self.label.set_text(lbl)
        self.progressbar.set_fraction(progress)

    getimages:
        gobject.idle_add(self.update_progress, lbl, prog)
		
	updateselected:
		i = 0
		for q in queue:
			if q[1] == selected[0]:
				threading.Thread(target=self.getimages(q)).start()
				break
			if i == len(queue) - 1:
				print("Could not find data for item: " + selected[0])
			else:
				i+=1
        # the GUI thread now returns to the mainloop
