# -*- generated by 1.0.9 -*-
import da
PatternExpr_192 = da.pat.TuplePattern([da.pat.ConstantPattern('res_get_current_configuration'), da.pat.FreePattern('config')])
PatternExpr_230 = da.pat.TuplePattern([da.pat.ConstantPattern('res_operation'), da.pat.FreePattern('result')])
PatternExpr_253 = da.pat.TuplePattern([da.pat.ConstantPattern('res_get_current_configuration'), da.pat.FreePattern('config')])
PatternExpr_271 = da.pat.TuplePattern([da.pat.ConstantPattern('res_operation'), da.pat.FreePattern('result')])
_config_object = {}

class Client(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_192, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_230, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_2', PatternExpr_253, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_252]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_3', PatternExpr_271, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Client_handler_270])])

    def setup(self, olympus, **rest_282):
        super().setup(olympus=olympus, **rest_282)
        self._state.olympus = olympus
        self._state.config = None

    def run(self):
        self.output('Client:>> Started')
        if (self._state.config is None):
            self.output('Client:>> Current Configuration is None')
            self.output('Client:>> Sending req_get_current_configuration to Olympus')
            self.send(('req_get_current_configuration', self._id), to=self._state.olympus)
            self.output('Client:>> Waiting for res_get_current_configuration from Olympus')
            super()._label('_st_label_189', block=False)
            config = None

            def ExistentialOpExpr_190():
                nonlocal config
                for (_, _, (_ConstantPattern206_, self._state.config)) in self._ClientReceivedEvent_0:
                    if (_ConstantPattern206_ == 'res_get_current_configuration'):
                        if True:
                            return True
                return False
            _st_label_189 = 0
            while (_st_label_189 == 0):
                _st_label_189 += 1
                if ExistentialOpExpr_190():
                    _st_label_189 += 1
                else:
                    super()._label('_st_label_189', block=True)
                    _st_label_189 -= 1
            self.output('Client:>> Ready to perform operation')
        self.output('Client:>> Already have headnode')
        self.send(('req_operation', self._id), to=self._state.config.list_replica[0])
        super()._label('_st_label_227', block=False)
        result = None

        def ExistentialOpExpr_228():
            nonlocal result
            for (_, _, (_ConstantPattern245_, result)) in self._ClientReceivedEvent_1:
                if (_ConstantPattern245_ == 'res_operation'):
                    if True:
                        return True
            return False
        _st_label_227 = 0
        while (_st_label_227 == 0):
            _st_label_227 += 1
            if ExistentialOpExpr_228():
                _st_label_227 += 1
            else:
                super()._label('_st_label_227', block=True)
                _st_label_227 -= 1

    def _Client_handler_252(self, config):
        self.output('Client:>> Received res_get_current_configuration from Olympus')
        self._state.config = config
        self.output('Client:>> current Configuration Updated')
    _Client_handler_252._labels = None
    _Client_handler_252._notlabels = None

    def _Client_handler_270(self, result):
        self.output('Client:>> Received res_operation from Replica')
        self.output('Client:>> Result of operation is ', result)
    _Client_handler_270._labels = None
    _Client_handler_270._notlabels = None
