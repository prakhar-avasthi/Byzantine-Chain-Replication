# -*- generated by 1.0.9 -*-
import da
PatternExpr_215 = da.pat.TuplePattern([da.pat.ConstantPattern('res_get_current_configuration'), da.pat.FreePattern('config')])
PatternExpr_353 = da.pat.TuplePattern([da.pat.ConstantPattern('res_operation'), da.pat.FreePattern('operation'), da.pat.FreePattern('result'), da.pat.FreePattern('result_proof_list')])
PatternExpr_389 = da.pat.ConstantPattern('terminate_client')
PatternExpr_407 = da.pat.TuplePattern([da.pat.ConstantPattern('res_get_current_configuration'), da.pat.FreePattern('config')])
PatternExpr_421 = da.pat.TuplePattern([da.pat.ConstantPattern('res_operation'), da.pat.FreePattern('operation'), da.pat.FreePattern('result'), da.pat.FreePattern('result_proof_list')])
_config_object = {}

class Client(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._ClientReceivedEvent_2 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_215, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_353, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_2', PatternExpr_389, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_3', PatternExpr_407, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_406]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_4', PatternExpr_421, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_420])])

    def setup(self, olympus, index, workload, timeout, **rest_438):
        super().setup(olympus=olympus, index=index, workload=workload, timeout=timeout, **rest_438)
        self._state.olympus = olympus
        self._state.index = index
        self._state.workload = workload
        self._state.timeout = timeout
        self._state.config = None
        self.output('Client', self._state.index, ':>> workload: ', self._state.workload)
        self._state.operations = None
        if (not ('random' in self._state.workload)):
            self._state.operations = self._state.workload.split(';')

    def run(self):
        self.output('Client', self._state.index, ':>> Started')
        if (self._state.config is None):
            self.send(('req_get_current_configuration', self._id), to=self._state.olympus)
            super()._label('_st_label_212', block=False)
            config = None

            def ExistentialOpExpr_213():
                nonlocal config
                for (_, _, (_ConstantPattern229_, self._state.config)) in self._ClientReceivedEvent_0:
                    if (_ConstantPattern229_ == 'res_get_current_configuration'):
                        if True:
                            return True
                return False
            _st_label_212 = 0
            while (_st_label_212 == 0):
                _st_label_212 += 1
                if ExistentialOpExpr_213():
                    _st_label_212 += 1
                else:
                    super()._label('_st_label_212', block=True)
                    _st_label_212 -= 1
        if (not (self._state.operations is None)):
            for command in self._state.operations:
                command = command.strip()
                class_operation = da.import_da('Operation')
                operation = class_operation.Operation()
                operation.client_request_id = self._state.index
                if ('put' in command):
                    operation.type = 1
                    operation.command = command[3:]
                elif ('get' in command):
                    operation.type = 2
                    operation.command = command[3:]
                elif ('slice' in command):
                    operation.type = 3
                    operation.command = command[5:]
                elif ('append' in command):
                    operation.type = 4
                    operation.command = command[6:]
                self.output('Client', self._state.index, ':>> Sending operation to Head Node: ', operation.command)
                self.send(('req_operation', operation, self._id, self._state.index), to=self._state.config.list_replica[0])
                super()._label('_st_label_350', block=False)
                result_proof_list = operation = result = None

                def ExistentialOpExpr_351():
                    nonlocal result_proof_list, operation, result
                    for (_, _, (_ConstantPattern371_, operation, result, result_proof_list)) in self._ClientReceivedEvent_1:
                        if (_ConstantPattern371_ == 'res_operation'):
                            if True:
                                return True
                    return False
                _st_label_350 = 0
                self._timer_start()
                while (_st_label_350 == 0):
                    _st_label_350 += 1
                    if ExistentialOpExpr_351():
                        pass
                        _st_label_350 += 1
                    elif self._timer_expired:
                        self.output('Client', self._state.index, ':>> Timeout: ', operation)
                        _st_label_350 += 1
                    else:
                        super()._label('_st_label_350', block=True, timeout=self._state.timeout)
                        _st_label_350 -= 1
                else:
                    if (_st_label_350 != 2):
                        continue
                if (_st_label_350 != 2):
                    break
        super()._label('l', block=False)

        def ExistentialOpExpr_387():
            for (_, _, _ConstantPattern400_) in self._ClientReceivedEvent_2:
                if (_ConstantPattern400_ == 'terminate_client'):
                    if True:
                        return True
            return False
        _st_label_386 = 0
        while (_st_label_386 == 0):
            _st_label_386 += 1
            if ExistentialOpExpr_387():
                _st_label_386 += 1
            else:
                super()._label('l', block=True)
                _st_label_386 -= 1

    def _Client_handler_406(self, config):
        self._state.config = config
    _Client_handler_406._labels = None
    _Client_handler_406._notlabels = None

    def _Client_handler_420(self, operation, result, result_proof_list):
        self.output('Client', self._state.index, ':>> Result of operation ', operation, ' is ', result)
    _Client_handler_420._labels = None
    _Client_handler_420._notlabels = None
