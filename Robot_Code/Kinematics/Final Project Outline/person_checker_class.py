

class PersonChecker(object):
    def __init__(self, handler):
        self.handler = handler
        self.object_check = None
        self.goal_blob = None

    def operate(self):
        object_list = self.handler.getObjects()
        if object_list == []:
            print "no objects"
            self.object_check = False
            return self.object_check

        blob_list = []

        for item in object_list:
            if "blob" in item.object_id:
                blob_list.append(item)

        if blob_list == []:
            print "no blobs"
            self.object_check = False
            return self.object_check

        blob_list.sort(key = lambda x: x.x_coord, reverse = True)

        # new_list = []
        # for item in blob_list:
        #     if item.x_coord < 50:
        #         new_list.append(item)
        new_list = [item for item in blob_list if item.x_coord < 50]

        # for item in range(len(blob_list) - 1):
        #     if blob_list[item].x_coord > 50:
        #         blob_list.pop(item)

        if blob_list == []:
            print "no blobs"
            self.object_check = False
            return self.object_check

        self.object_check = True

        self.goal_blob = blob_list[-1]

        return self.object_check

    def get_goal_blob(self):
        return self.goal_blob
