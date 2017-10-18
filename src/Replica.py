# -*- generated by 1.0.9 -*-
import da
PatternExpr_183 = da.pat.ConstantPattern('terminate_replica')
PatternExpr_329 = da.pat.TuplePattern([da.pat.ConstantPattern('req_operation'), da.pat.FreePattern('operation'), da.pat.FreePattern('client'), da.pat.FreePattern('client_index')])
PatternExpr_494 = da.pat.TuplePattern([da.pat.ConstantPattern('result_shuttle'), da.pat.FreePattern('replica'), da.pat.FreePattern('result_shuttle')])
PatternExpr_528 = da.pat.TuplePattern([da.pat.ConstantPattern('forward_shuttle'), da.pat.FreePattern('replica'), da.pat.FreePattern('forward_shuttle'), da.pat.FreePattern('client')])
PatternExpr_656 = da.pat.TuplePattern([da.pat.ConstantPattern('result_shuttle'), da.pat.FreePattern('replica'), da.pat.FreePattern('result_shuttle')])
PatternExpr_820 = da.pat.TuplePattern([da.pat.ConstantPattern('forward_shuttle'), da.pat.FreePattern('replica'), da.pat.FreePattern('forward_shuttle'), da.pat.FreePattern('client')])
PatternExpr_854 = da.pat.TuplePattern([da.pat.ConstantPattern('result_shuttle'), da.pat.FreePattern('replica'), da.pat.FreePattern('result_shuttle')])
PatternExpr_916 = da.pat.TuplePattern([da.pat.ConstantPattern('forward_shuttle'), da.pat.FreePattern('replica'), da.pat.FreePattern('forward_shuttle'), da.pat.FreePattern('client')])
_config_object = {}

class Replica(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ReplicaReceivedEvent_0 = []
        self._ReplicaReceivedEvent_2 = []
        self._ReplicaReceivedEvent_4 = []
        self._ReplicaReceivedEvent_5 = []
        self._ReplicaReceivedEvent_7 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_0', PatternExpr_183, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_1', PatternExpr_329, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_328]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_2', PatternExpr_494, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_3', PatternExpr_528, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_527]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_4', PatternExpr_656, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_5', PatternExpr_820, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_6', PatternExpr_854, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Replica_handler_853]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ReplicaReceivedEvent_7', PatternExpr_916, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, olympus, replicaList, index, type, database, history, timeout, **rest_949):
        super().setup(olympus=olympus, replicaList=replicaList, index=index, type=type, database=database, history=history, timeout=timeout, **rest_949)
        self._state.olympus = olympus
        self._state.replicaList = replicaList
        self._state.index = index
        self._state.type = type
        self._state.database = database
        self._state.history = history
        self._state.timeout = timeout
        pass

    def run(self):
        self.output('Replica', self._state.index, ':>> Replica Started: ', self._state.type)
        super()._label('_st_label_180', block=False)

        def ExistentialOpExpr_181():
            for (_, _, _ConstantPattern194_) in self._ReplicaReceivedEvent_0:
                if (_ConstantPattern194_ == 'terminate_replica'):
                    if True:
                        return True
            return False
        _st_label_180 = 0
        while (_st_label_180 == 0):
            _st_label_180 += 1
            if ExistentialOpExpr_181():
                _st_label_180 += 1
            else:
                super()._label('_st_label_180', block=True)
                _st_label_180 -= 1

    def performOperation(self, operation):
        self.output('Replica', self._state.index, ':>> perform operation: ', operation.command)
        import re
        matches = re.findall("\\'(.+?)\\'", operation.command)
        key = None
        value = None
        if (not (operation.type is 2)):
            key = matches[0]
            value = matches[1]
        else:
            key = matches[0]
        if (operation.type is 1):
            self._state.database[key] = value
            return 'OK'
        elif (operation.type is 2):
            if (key in self._state.database):
                return self._state.database[key]
            else:
                return ''
        elif (operation.type is 3):
            return 'OK'
        elif (operation.type is 4):
            if (key in self._state.database):
                val = self._state.database[key]
                list_val = (val + value)
                self._state.database[key] = list_val
                return 'OK'
            else:
                return 'FAIL'

    def _Replica_handler_328(self, operation, client, client_index):
        self.output('Replica', self._state.index, ':>> Received req_operation from Client', client_index, ' operation: ', operation.command)
        result = self.performOperation(operation)
        if (self._state.type == 'head'):
            class_action = da.import_da('Action')
            action = class_action.Action()
            action.seq_id = 1
            action.operation = operation
            order_proof_list = []
            result_proof_list = []
            class_order_proof = da.import_da('OrderProof')
            order_proof = class_order_proof.OrderProof()
            order_proof.order = 'order'
            order_proof.action = action
            order_proof_list.append(order_proof)
            class_result_proof = da.import_da('ResultProof')
            result_proof = class_result_proof.ResultProof()
            result_proof.result_const = 'result'
            result_proof.action = action
            result_proof.result = result
            result_proof_list.append(result_proof)
            class_shuttle = da.import_da('Shuttle')
            forward_shuttle = class_shuttle.Shuttle()
            forward_shuttle.action = action
            forward_shuttle.order_proof_list = order_proof_list
            forward_shuttle.result_proof_list = result_proof_list
            self.output('Replica', self._state.index, ':>> Forwarding shuttle to Replica', (self._state.index + 1), ' operation: ', action.operation.command)
            self.send(('forward_shuttle', self._id, forward_shuttle, client), to=self._state.replicaList[(self._state.index + 1)])
            super()._label('_st_label_491', block=False)
            replica = result_shuttle = None

            def ExistentialOpExpr_492():
                nonlocal replica, result_shuttle
                for (_, _, (_ConstantPattern511_, replica, result_shuttle)) in self._ReplicaReceivedEvent_2:
                    if (_ConstantPattern511_ == 'result_shuttle'):
                        if True:
                            return True
                return False
            _st_label_491 = 0
            self._timer_start()
            while (_st_label_491 == 0):
                _st_label_491 += 1
                if ExistentialOpExpr_492():
                    pass
                    _st_label_491 += 1
                elif self._timer_expired:
                    self.output('Replica', self._state.index, ':>> Replica timedout')
                    _st_label_491 += 1
                else:
                    super()._label('_st_label_491', block=True, timeout=self._state.timeout)
                    _st_label_491 -= 1
    _Replica_handler_328._labels = None
    _Replica_handler_328._notlabels = None

    def _Replica_handler_527(self, replica, forward_shuttle, client):
        action = forward_shuttle.action
        self.output('Replica', self._state.index, ':>> Received forward_shuttle from previous replica, operation: ', action.operation.command)
        result = self.performOperation(action.operation)
        if (self._state.type == 'normal_replica'):
            order_proof_list = forward_shuttle.order_proof_list
            result_proof_list = forward_shuttle.result_proof_list
            class_order_proof = da.import_da('OrderProof')
            order_proof = class_order_proof.OrderProof()
            order_proof.order = 'order'
            order_proof.action = action
            order_proof_list.append(order_proof)
            class_result_proof = da.import_da('ResultProof')
            result_proof = class_result_proof.ResultProof()
            result_proof.result_const = 'result'
            result_proof.action = action
            result_proof.result = result
            result_proof_list.append(result_proof)
            self.output('Replica', self._state.index, ':>> Forwarding shuttle to Replica: ', (self._state.index + 1), ' operation: ', action.operation.command)
            self.send(('forward_shuttle', self._id, forward_shuttle, client), to=self._state.replicaList[(self._state.index + 1)])
            super()._label('_st_label_653', block=False)
            result_shuttle = replica = None

            def ExistentialOpExpr_654():
                nonlocal result_shuttle, replica
                for (_, _, (_ConstantPattern672_, replica, result_shuttle)) in self._ReplicaReceivedEvent_4:
                    if (_ConstantPattern672_ == 'result_shuttle'):
                        if True:
                            return True
                return False
            _st_label_653 = 0
            self._timer_start()
            while (_st_label_653 == 0):
                _st_label_653 += 1
                if ExistentialOpExpr_654():
                    pass
                    _st_label_653 += 1
                elif self._timer_expired:
                    self.output('Replica', self._state.index, ':>> Replica timedout')
                    _st_label_653 += 1
                else:
                    super()._label('_st_label_653', block=True, timeout=self._state.timeout)
                    _st_label_653 -= 1
        if (self._state.type == 'tail'):
            self.send(('res_operation', action.operation.command, result, forward_shuttle.result_proof_list), to=client)
            self.output('Replica', self._state.index, ':>> Replied res_operation to Client: ', action.operation.command, ' result: ', result)
            order_proof_list = forward_shuttle.order_proof_list
            result_proof_list = forward_shuttle.result_proof_list
            class_order_proof = da.import_da('OrderProof')
            order_proof = class_order_proof.OrderProof()
            order_proof.order = 'order'
            order_proof.action = action
            order_proof_list.append(order_proof)
            class_result_proof = da.import_da('ResultProof')
            result_proof = class_result_proof.ResultProof()
            result_proof.result_const = 'result'
            result_proof.action = action
            result_proof.result = result
            result_proof_list.append(result_proof)
            class_shuttle = da.import_da('Shuttle')
            result_shuttle = class_shuttle.Shuttle()
            result_shuttle.action = action
            result_shuttle.order_proof_list = order_proof_list
            result_shuttle.result_proof_list = result_proof_list
            self.output('Replica', self._state.index, ':>> Sending result shuttle back to replica: ', (self._state.index - 1), ' operation: ', action.operation.command)
            self.send(('result_shuttle', self._id, result_shuttle), to=self._state.replicaList[(self._state.index - 1)])
            super()._label('_st_label_817', block=False)
            client = forward_shuttle = replica = None

            def ExistentialOpExpr_818():
                nonlocal client, forward_shuttle, replica
                for (_, _, (_ConstantPattern836_, replica, forward_shuttle, client)) in self._ReplicaReceivedEvent_5:
                    if (_ConstantPattern836_ == 'forward_shuttle'):
                        if True:
                            return True
                return False
            _st_label_817 = 0
            self._timer_start()
            while (_st_label_817 == 0):
                _st_label_817 += 1
                if ExistentialOpExpr_818():
                    pass
                    _st_label_817 += 1
                elif self._timer_expired:
                    self.output('Replica', self._state.index, ':>> Replica timedout')
                    _st_label_817 += 1
                else:
                    super()._label('_st_label_817', block=True, timeout=self._state.timeout)
                    _st_label_817 -= 1
    _Replica_handler_527._labels = None
    _Replica_handler_527._notlabels = None

    def _Replica_handler_853(self, replica, result_shuttle):
        action = result_shuttle.action
        self._state.history[action] = result_shuttle
        self.output('Replica', self._state.index, ':>> Received result_shuttle from previous replica: ', action.operation.command)
        if (not (self._state.type == 'head')):
            self.output('Replica', self._state.index, ':>> Sending result shuttle back to replica: ', (self._state.index - 1), ' operation: ', action.operation.command)
            self.send(('result_shuttle', self._id, result_shuttle), to=self._state.replicaList[(self._state.index - 1)])
            super()._label('_st_label_913', block=False)
            replica = client = forward_shuttle = None

            def ExistentialOpExpr_914():
                nonlocal replica, client, forward_shuttle
                for (_, _, (_ConstantPattern934_, replica, forward_shuttle, client)) in self._ReplicaReceivedEvent_7:
                    if (_ConstantPattern934_ == 'forward_shuttle'):
                        if True:
                            return True
                return False
            _st_label_913 = 0
            self._timer_start()
            while (_st_label_913 == 0):
                _st_label_913 += 1
                if ExistentialOpExpr_914():
                    pass
                    _st_label_913 += 1
                elif self._timer_expired:
                    self.output('Replica', self._state.index, ':>> Replica timedout')
                    _st_label_913 += 1
                else:
                    super()._label('_st_label_913', block=True, timeout=self._state.timeout)
                    _st_label_913 -= 1
    _Replica_handler_853._labels = None
    _Replica_handler_853._notlabels = None
