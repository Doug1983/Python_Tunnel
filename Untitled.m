clear classes
clc
module = py.importlib.import_module('ML_MatlabTcpTunnel');
py.importlib.reload(module);

pyObj = py.ML_MatlabTcpTunnel.ML_MatlabTcpTunnel('127.0.0.1', uint16(1666), uint16(2^16), '\r\n', 1.00);

%%
if (pyObj.Connect())
   %pyObj.SendMessage('Test');
else
   a=0 
end

%% 
tic
test = num2str(rand(1,500));
Status = pyObj.SendMessage(test);

if Status
    Message = pyObj.ReceiveMessage();
end
toc

%%

pyObj.Close()